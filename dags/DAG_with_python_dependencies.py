from airflow import DAG
from datetime import timedelta, datetime
from airflow.operators.python import PythonOperator


def_args = {
    "owner":"Dan4sure",
    'retris':5,
    'retry_delay': timedelta(seconds=15)
}