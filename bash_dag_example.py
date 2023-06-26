from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

default_args = {
    'start_date': datetime(2023, 6, 26)
}

dag = DAG(
    'bash_dag',
    default_args=default_args,
    schedule_interval=None,
)

dummy_task = BashOperator(
    task_id='dummy_task',
    bash_command='echo "This is a dummy task"',
    dag=dag,
)

dummy_task >> bash_task