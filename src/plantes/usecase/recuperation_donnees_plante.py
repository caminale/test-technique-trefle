import logging

from src.plantes.infrastructure.plante_api import PlanteApi
from src.plantes.infrastructure.trefle_api import TrefleApi

logger = logging.getLogger(__name__)


class RecuperationDonneesDePlantes:
    def __init__(self, from_api: PlanteApi):
        self.api = from_api

    def execute(self):
        self.api.recuperation_des_donnees_plantes()


def main():
    api = TrefleApi()
    uc = RecuperationDonneesDePlantes(from_api=api)
    uc.execute()


if __name__ == '__main__':
    main()
