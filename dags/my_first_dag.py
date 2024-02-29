from datetime import datetime, timedelta
from airflow import DAG
import airflow
from airflow.operators.bash import BashOperator

default_args = {
    'owner':"Dan4sure",
    'retries': 5,
    'retry_delay': timedelta(seconds=10)
}


with DAG(
    dag_id = "my_first_dag_v4.1.1",
    default_args = default_args,
    description = "this is my first dag I am writing",
    start_date = datetime(2024, 2, 25, 3),
    schedule_interval = '@daily'
) as dag:
    task1 = BashOperator(
        task_id="first_task",
        bash_command="echo hello world, this is the first task!"
    )

    task2 = BashOperator(
        task_id="second_task",
        bash_command="echo Hey, I am the second task and will be running after task 1"
    )


    task3 = BashOperator(
        task_id = "third_task",
        bash_command="echo This is task 3, I will be running concurrently with task 2"
    )
    # task1.set_downstream(task2)
    # task1.set_downstream(task3)

    # second method
    # task1 >> task2
    # task1 >> task3

    # third method
    task1 >> [task2, task3]