USE plantesdb;
COPY into plante
FROM @STAGE_PLANTE_S3/plantes/
    pattern='.*[.]parquet'
    MATCH_BY_COLUMN_NAME = CASE_INSENSITIVE;