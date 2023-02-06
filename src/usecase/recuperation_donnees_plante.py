import logging

import pandas as pd

from src.infrastructure.plante_api import PlanteApi
from src.infrastructure.stockage_client import StockageClient

logger = logging.getLogger(__name__)


class RecuperationDonneesDePlantes:
    def __init__(self, from_api: PlanteApi, stockage_client: StockageClient):
        self.stockage_client = stockage_client
        self.api = from_api

    def execute(self):
        numero_premiere_page, numero_derniere_page = self.api.get_premiere_et_derniere_page()
        df = pd.DataFrame()
        for page in range(numero_premiere_page, numero_derniere_page + 1):
            logger.info(f"Nous sommes à la récupération de la page numéro : {page}")
            current_page_df = pd.DataFrame(self.api.recuperation_donnees_plantes_par_page(page))
            df = pd.concat([current_page_df, df])
            if page == numero_derniere_page:
                self.stockage_client.on_sauvegarde(df)
                break
            self.stockage_client.toute_les_n_pages_on_sauvegarde(df=df, numero_page_courrante=page,
                                                                 max_page=500)
