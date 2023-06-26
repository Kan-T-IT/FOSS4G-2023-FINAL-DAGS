from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.docker_operator import DockerOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 6, 26),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
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

docker_task = DockerOperator(
    task_id='docker_task',
    image='hello-world',
    auto_remove=True,
    docker_url='tcp://host.docker.internal:2375',
    api_version='auto',
    dag=dag,
)

dummy_task >> docker_task