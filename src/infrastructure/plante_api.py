from abc import ABC


class PlanteApi(ABC):
    def get_premiere_et_derniere_page(self):
        pass

    def recuperation_donnees_plantes_par_page(self, page):
        pass
