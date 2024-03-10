from airflow import DAG
from datetime import timedelta, datetime
from airflow.operators.python import PythonOperator
from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor


def_args = {
    "owner":"Dan4sure",
    'retris':5,
    'retry_delay': timedelta(minutes=1)
} 


with DAG (
    default_args=def_args,
    dag_id="DAG_with_minio_s3_v.1",
    description="my first DAG using python operator",
    start_date=datetime(2024, 3, 3, 6),
    schedule_interval="@daily"
) as dag:

    task1 = S3KeySensor(
        task_id='sensor_minio_s3',
        bucket_name='airflow',
        bucket_key='Online_Retail.csv',
        aws_conn_id=''
    )
