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
def greet_time(age, ti):
    name = ti.xcom_pull(task_ids="get_name")
    now = datetime.now()
    format = '%H:%M:%S - %d/%m/%Y'
    print(f"\nHello everyone at {datetime.strftime(now, format)} \nMy name is {name} and I am {age} years old.")


# using XCOMs
def name():
    return "Daniel Ezeh"



with DAG (
    default_args=def_args,
    dag_id="my_DAG_with_python_operator_v04.8",
    description="my first DAG using python operator",
    start_date=datetime(2024, 2, 25, 6),
    schedule_interval="@daily"
) as dag:
    
    task2 = PythonOperator(
        task_id = "greeting_time",
        python_callable=greet_time,
        op_kwargs={
            'age':19
        }
    )


    task1 = PythonOperator(
        task_id = "get_name",
        python_callable=name,
    )

    task1 >> task2