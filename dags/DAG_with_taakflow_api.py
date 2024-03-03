from airflow.decorators import dag, task
from datetime import datetime, timedelta


now = datetime.now()
format = '%H:%M:%S - %d/%m/%Y'
my_time = datetime.strftime(now, format)

def_args = {
    'owner':'Dan4sure',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}


@dag(
    dag_id="dag_with_taskflow_api_v01",
    start_date=datetime(2024,3,1),
    schedule_interval="@daily"
)

def hello_world_etl():

    @task()
    def get_name():
        return "Daniel"
    
    @task()
    def get_age():
        return 20
    
    @task()
    def greeting(name, age):
        print(f'Hello at {my_time}, my name is {name}'
              f'and I am {age} years old.')
    
    name = get_name()
    age = get_age()
    greeting(name, age)


greet_dag = hello_world_etl()
