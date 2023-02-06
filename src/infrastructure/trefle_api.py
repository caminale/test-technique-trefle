import logging
import os
from pathlib import Path
from time import sleep

import requests
from marshmallow import INCLUDE, ValidationError

from src.infrastructure.dtos.PlanteSchema import PlanteSchema
from src.infrastructure.plante_api import PlanteApi

logger = logging.getLogger(__name__)


class TrefleApi(PlanteApi):
    def __init__(self):
        self.base_url = "https://trefle.io/api/v1/plants"
        self.url = requests.get(self.base_url, params={"token": "xxxx"}).url

    def get_premiere_et_derniere_page(self) -> (int, int):
        resultat_brut = requests.get(self.url).json()
        numero_premiere_page = resultat_brut.get("links").get("first").split("=")[1]
        numero_derniere_page = resultat_brut.get("links").get("last").split("=")[1]
        return int(numero_premiere_page), int(numero_derniere_page)

    def recuperation_donnees_plantes_par_page(self, numero_page: int):
        try:
            plantes_format_brute = requests.get(self.url, params={"page": numero_page}).json().get("data")
            sleep(.5)
            plantes = list(map(lambda plante: PlanteSchema().load(plante, unknown=INCLUDE), plantes_format_brute))
            return plantes
        except ValidationError as error:
            logger.warning(
                    f"Une enregistrement de plante ne colle pas au schema: {error.messages}"
            )
            pass
