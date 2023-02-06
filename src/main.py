from airflow.providers.amazon.aws.hooks.base_aws import AwsBaseHook

from src.infrastructure.s3_client import S3Client
from src.infrastructure.trefle_api import TrefleApi
from src.usecase.recuperation_donnees_plante import RecuperationDonneesDePlantes


def recuperation_donnees_plantes_depuis_trefle():
    hook = AwsBaseHook(aws_conn_id="aws")
    session = hook.get_session()
    api = TrefleApi()
    stockage = S3Client(s3_session=session)
    uc = RecuperationDonneesDePlantes(from_api=api, stockage_client=stockage)
    uc.execute()
