from datetime import datetime, timedelta
from airflow import DAG
import airflow
from airflow.operators.bash import BashOperator

default_args = {
    'owner':"Dan4sure",
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}


with DAG (
    dag_id = "my_first_dag_v2",
    default_args = default_args,
    description = "this is my first dag I am writing",
    start_date = datetime(2024, 2, 15, 3),
    schedule_interval = '@daily'
) as dag:
    task1 = BashOperator(
        task_id="first_task",
        bash_command="echo hello world, this is the first task!"
    )

    task2 = BashOperator(
        task_id="second_task",
        bash_command="echo Hey, I'm the second task and will be running after task 1"
    )

    task1.set_downstream(task2)