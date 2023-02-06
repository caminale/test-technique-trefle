import datetime

import awswrangler
import pandas as pd

from src.infrastructure.stockage_client import StockageClient

class S3Client(StockageClient):
    def __init__(self, s3_session):
        self.s3_session = s3_session

    def on_sauvegarde(self, df: pd.DataFrame):
        awswrangler.s3.to_parquet(df, path="s3://trefle-plants/plantes",
                                  boto3_session=self.s3_session,
                                  dataset=True
                                  )

    def toute_les_n_pages_on_sauvegarde(self, df, numero_page_courrante, max_page: int):
        if numero_page_courrante % max_page == 0:
            self.on_sauvegarde(df)
