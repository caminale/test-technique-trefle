import datetime

from airflow import DAG
from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator

with DAG(
        dag_id="ingestion_donnees_plantes_dans_snowflake",
        catchup=False,
        dagrun_timeout=datetime.timedelta(minutes=20),
) as dag:
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
            creation_table_plante_snowflake
            >> chargement_donnees_plantes_vers_snowflake
    )
