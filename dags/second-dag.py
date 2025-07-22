from airflow.decorators import dag, task
from datetime import datetime
import os
import shutil

SOURCE_PATH = '/opt/airflow/test.csv'
DESTINATION_DIR = '/opt/airflow'
DESTINATION_PATH = os.path.join(DESTINATION_DIR, 'data.csv')

@dag(
    dag_id='move_local_csv_dag_v3',
    start_date=datetime(2023, 1, 1),
    schedule=None,  # Manual run
    catchup=False,
    tags=['example', 'local_file'],
)
def move_csv_file():

    @task
    def check_file():
        if not os.path.exists(SOURCE_PATH):
            raise FileNotFoundError(f"File not found: {SOURCE_PATH}")
        return SOURCE_PATH

    @task
    def copy_file(src_path: str):
        os.makedirs(DESTINATION_DIR, exist_ok=True)
        shutil.copy2(src_path, DESTINATION_PATH)
        return DESTINATION_PATH

    src = check_file()
    copy_file(src)

dag = move_csv_file()
