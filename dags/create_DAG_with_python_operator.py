from airflow import DAG
from datetime import timedelta, datetime
from airflow.operators.python import PythonOperator

def_args = {
    "owner":"Dan4sure",
    'retris':5,
    'retry_delay': timedelta(seconds=15)
}


# Defining a function that want to run in python
def greet_time():
    now = datetime.now()
    format = '%H:%M:%S - %d/%m/%Y'
    print(f"Hello everyone at {datetime.strftime(now, format)}")



with DAG (
    default_args=def_args,
    dag_id="my_DAG_with_python_operator_v01",
    description="my first DAG using python operator",
    start_date=datetime(2024, 2, 25, 6),
    schedule_interval="@daily"
) as DAG:
    task1 = PythonOperator(
        task_id = "greeting_time",
        python_callable=greet_time
    )

    task1