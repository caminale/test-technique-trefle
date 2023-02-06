CREATE OR REPLACE file format parquetformat type = 'PARQUET';
CREATE STAGE IF NOT EXISTS STAGE_PLANTE_S3
    url = 's3://bucket-name'
    file_format = parquetformat
    credentials = (aws_secret_key = 'xxx' aws_key_id = 'xx');
