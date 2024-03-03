from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator


def_args = {
    "owner":"Dan4sure",
    'retris':5,
    'retry_delay': timedelta(seconds=15)
}

with DAG(
     dag_id="dag_with_postgre_operator_v02.4",
     default_args=def_args,
     start_date=datetime(2024,3,1),
     schedule_interval='0 0 * * *'
) as dag:
    
    task1 = PostgresOperator(
        task_id='create_postgres_table',
        postgres_conn_id="postgres_localhost",
        sql='''
            create table if not exists dag_runs (
            dt date,
            dag_id character varying,
            primary key (dt, dag_id)
            )
        '''
    )


    task2 = PostgresOperator(
        task_id="inserting_data_into_table",
        postgres_conn_id="postgres_localhost",
        sql = '''
            insert into dag_runs (dt, dag_id) values ('{{ds}}', '{{dag.dag_id}}')
        '''
    )


    task3 = PostgresOperator(
        task_id="deleting_data_from_table",
        postgres_conn_id="postgres_localhost",
        sql = '''
            delete from dag_runs where dt = '{{ds}}' and dag_id ='{{dag.dag_id}};'
        '''
    )

    task1 >> task3 >> task2