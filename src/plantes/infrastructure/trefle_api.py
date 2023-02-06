import os
from pathlib import Path
from time import sleep

import pandas as pd
import pyarrow as pa
import requests
from marshmallow import INCLUDE, ValidationError
from pyarrow import parquet as pq

from src.plantes.usecase.recuperation_donnees_plante import logger
from src.plantes.infrastructure.dtos.PlanteSchema import PlanteSchema
from src.plantes.infrastructure.plante_api import PlanteApi


class TrefleApi(PlanteApi):
    def __init__(self):
        self.base_url = "https://trefle.io/api/v1/plants"
        self.token = "xxxxx"
        self.url = requests.get(self.base_url, params={"token": self.token}).url

    def recuperation_des_donnees_plantes(self):
        numero_premiere_page, numero_derniere_page = self.connaitre_premiere_et_derniere_page()
        df = pd.DataFrame()
        for page in range(0, numero_derniere_page + 1):
            logger.info(f"Nous sommes à la récupération de la page numéro : {page}")
            current_page_df = pd.DataFrame(self.recuperation_donnees_plantes_par_page(page))
            df = pd.concat([current_page_df, df])
            sleep(.2)
            print(page, numero_derniere_page)
            if page == numero_derniere_page:
                self.on_sauvegarde(df, page)
                break
            self.toute_les_n_pages_on_sauvegarde(df, page, 120)

    def toute_les_n_pages_on_sauvegarde(self, df, numero_page_courrante, max_page: int):
        if numero_page_courrante % max_page == 0:
            self.on_sauvegarde(df, numero_page_courrante)
            df = pd.DataFrame()
        return df

    def on_sauvegarde(self, df, numero_page_courrante):
        path = f"{self.__get_path()}/{numero_page_courrante}-trefle.parquet"
        table = pa.Table.from_pandas(df=df)
        pq.write_table(table, path)

    def connaitre_premiere_et_derniere_page(self) -> (int, int):
        resultat_brut = requests.get(self.url).json()
        numero_premiere_page = resultat_brut.get("links").get("first").split("=")[1]
        numero_derniere_page = resultat_brut.get("links").get("last").split("=")[1]
        return int(numero_premiere_page), int(numero_derniere_page)

    def recuperation_donnees_plantes_par_page(self, numero_page: int):
        try:
            plantes_format_brute = requests.get(self.url, params={"page": numero_page}).json().get("data")
            plantes = list(map(lambda plante: PlanteSchema().load(plante, unknown=INCLUDE), plantes_format_brute))
            return plantes
        except ValidationError as error:
            logger.warning(
                    f"Une enregistrement de plante ne colle pas au schema: {error.messages}"
            )
            pass

    def __get_path(self):
        root_path = Path(__file__).parent.parent.parent
        return os.path.join(root_path, "output")
