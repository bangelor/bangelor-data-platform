import datetime

from airflow.sdk import DAG
from airflow.providers.standard.operators.empty import EmptyOperator

with DAG(
    dag_id="firstDag",
    start_date=datetime.datetime(2025, 1, 1),
    schedule="@hourly",
):
    EmptyOperator(task_id="task")
print('hello')