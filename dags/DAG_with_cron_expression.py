from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator

def_args = {
    "owner":"Dan4sure",
    'retris':5,
    'retry_delay': timedelta(seconds=15)
}


# crone expression
# '0 0 * * *' = daily
# use "www.crontab.guru" for easily creating cron schedule


with DAG(
    default_args = def_args,
    dag_id = 'dag_with_cron_expression_v02.3',
    start_date = datetime(2024,2,25),
    schedule_interval = '0 3 * * Tue-fri'
) as dag:

    task1 = BashOperator(
        task_id =  'task1',
        bash_command = 'echo dag with cron expression'
    )
    task1