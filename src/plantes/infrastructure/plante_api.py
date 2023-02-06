from abc import ABC, abstractmethod


class PlanteApi(ABC):
    @abstractmethod
    def recuperation_des_donnees_plantes(self):
        pass
