FROM apache/airflow:2.5.1-python3.10
COPY requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt
