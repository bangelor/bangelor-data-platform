FROM apache/airflow:3.0.3
COPY requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt