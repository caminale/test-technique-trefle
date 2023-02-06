import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator

from src.main import recuperation_donnees_plantes_depuis_trefle

with DAG(
        dag_id="ingestion_donnees_plantes_dans_snowflake",
        catchup=False,
        start_date=datetime.datetime(2023, 2, 5),
        dagrun_timeout=datetime.timedelta(minutes=240),
) as dag:
    recuperation_donnees_plantes = PythonOperator(
            task_id="recuperation_donnees_plantes",
            python_callable=recuperation_donnees_plantes_depuis_trefle,
            dag=dag,
    )

    creation_table_plante_snowflake = SnowflakeOperator(
            task_id="creation_table_plante_snowflake",
            sql="./scripts-sql/creation_table_plante.sql",
            snowflake_conn_id="snowflake",
            dag=dag,
    )

    chargement_donnees_plantes_vers_snowflake = SnowflakeOperator(
            task_id="chargement_donnees_plantes_s3_vers_snowflake",
            sql="./scripts-sql/copier_donnees_s3_vers_snowflake.sql",
            snowflake_conn_id="snowflake",
            dag=dag,
    )

    (
            recuperation_donnees_plantes
            >> creation_table_plante_snowflake
            >> chargement_donnees_plantes_vers_snowflake
    )
