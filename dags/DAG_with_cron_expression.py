from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator

def_args = {
    "owner":"Dan4sure",
    'retris':5,
    'retry_delay': timedelta(seconds=15)
}


with DAG(
    default_args = def_args,
    dag_id = 'dag_with_cron_expression_v01',
    start_date = datetime(2024,2,25),
    schedule_interval = '@daily'
) as dag:

    task1 = BashOperator(
        task_id =  'task1',
        bash_command = 'echo dag with cron expression'
    )
    task1