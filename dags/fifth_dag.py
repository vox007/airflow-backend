from datetime import datetime

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator

def print_hello():
    return 'Hello world from first Airflow DAG! allow fox'


dag = DAG('fifth_dag', description='Hello World DAG',
          schedule_interval=None,
          start_date=datetime(2022, 4, 13), is_paused_upon_creation=False)

hello_operator = PythonOperator(task_id='hello_task', python_callable=print_hello, dag=dag)

hello_operator