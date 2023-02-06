USE PLANTESDB;

CREATE OR REPLACE file format parquetformat type = 'PARQUET';

CREATE STAGE IF NOT EXISTS STAGE_PLANTE_S3
    url = 's3://bucket-name'
    file_format = parquetformat
    credentials = (aws_secret_key = 'xxx' aws_key_id = 'xx');

CREATE OR REPLACE TABLE PLANTE(
   id                 INTEGER  NOT NULL PRIMARY KEY
  ,common_name        VARCHAR(255)
  ,slug               VARCHAR(255)
  ,scientific_name    VARCHAR(255)
  ,year               INTEGER
  ,bibliography       VARCHAR(1000)
  ,author             VARCHAR(255)
  ,status             VARCHAR(255)
  ,rank               VARCHAR(255)
  ,family_common_name VARCHAR(255)
  ,genus_id           INTEGER
  ,image_url          VARCHAR(255)
  ,synonyms           ARRAY
  ,genus              VARCHAR(255)
  ,family             VARCHAR(255)
  ,links              ARRAY
);
