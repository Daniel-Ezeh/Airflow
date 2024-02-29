from airflow import DAG
from datetime import timedelta, datetime
from airflow.operators.python import PythonOperator

def_args = {
    "owner":"Dan4sure",
    'retris':5,
    'retry_delay': timedelta(seconds=15)
}


# Defining a function that want to run in python
# Adding a parameters to the function
def greet_time(name, age):
    now = datetime.now()
    format = '%H:%M:%S - %d/%m/%Y'
    print(f"Hello everyone at {datetime.strftime(now, format)} \nMy name is {name} and I am {age} years old.")



with DAG (
    default_args=def_args,
    dag_id="my_DAG_with_python_operator_v02",
    description="my first DAG using python operator",
    start_date=datetime(2024, 2, 25, 6),
    schedule_interval="@daily"
) as DAG:
    task1 = PythonOperator(
        task_id = "greeting_time",
        python_callable=greet_time,
        op_kwargs={
            'name':'Micheal James',
            'age':19
        }
    )

    task1