from airflow.decorators import dag, task
from datetime import datetime
import duckdb
import os

SOURCE_PATH = '/opt/airflow/source_data/test.csv'
DESTINATION_DIR = '/opt/airflow/target_data'

@dag(
    dag_id='csv_to_delta_duckdb',
    start_date=datetime(2023, 1, 1),
    schedule=None,
    catchup=False,
    tags=['duckdb', 'delta', 'csv'],
)
def csv_to_delta():

    @task
    def convert_to_delta():
        # Ensure destination dir exists
        os.makedirs(DESTINATION_DIR, exist_ok=True)

        # Connect to DuckDB in-memory
        con = duckdb.connect()

        # Load CSV and write to Delta
        con.execute(f"""
            INSTALL 'delta';
            LOAD 'delta';
            CREATE OR REPLACE TABLE data AS 
            SELECT * FROM read_csv_auto('{SOURCE_PATH}');
            COPY data TO '{DESTINATION_DIR}' (FORMAT DELTA);
        """)

    convert_to_delta()

dag = csv_to_delta()
