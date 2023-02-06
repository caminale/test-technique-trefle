from abc import ABC

import pandas as pd


class StockageClient(ABC):
    def on_sauvegarde(self, df: pd.DataFrame):
        pass

    def toute_les_n_pages_on_sauvegarde(self, **kwargs):
        pass
