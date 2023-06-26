from airflow import DAG
from airflow.operators.docker_operator import DockerOperator
from datetime import datetime
from docker.types import Mount


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 6, 26),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

dag = DAG('grass_docker_operator', default_args=default_args)

ndvi = DockerOperator(
    task_id='grass_docker_task',
    #image='hello-world',
    image='mundialis/grass-py3-pdal:8.2.1-alpine',
    api_version='auto',
    auto_remove=True,
    docker_url=f'tcp://host.docker.internal:2375',
    mount_tmp_dir=False,
    #command='bash ls /grassdb',
    #command='i.vi red=B04 nir=B08 viname=ndvi output=NDVI --overwrite && v.buffer input=highways output=highways_buffer distance=30 --overwrite && r.mask vector=highways_buffer',
    command='grass /grassdb/test/PERMANENT --exec bash /grassdb/scripts/ndvi.sh ',
    dag=dag,
    mounts=[Mount(source="\\\\wsl.localhost\\Ubuntu\\opt\\grass\\grassdata", target="/grassdb", type="bind")],
)

buffer = DockerOperator(
    task_id='grass_docker_task_buffer',
    #image='hello-world',
    image='mundialis/grass-py3-pdal:8.2.1-alpine',
    api_version='auto',
    auto_remove=True,
    docker_url=f'tcp://host.docker.internal:2375',
    mount_tmp_dir=False,
    #command='bash ls /grassdb',
    #command='i.vi red=B04 nir=B08 viname=ndvi output=NDVI --overwrite && v.buffer input=highways output=highways_buffer distance=30 --overwrite && r.mask vector=hi>
    command='grass /grassdb/test/PERMANENT --exec bash /grassdb/scripts/buffer.sh ',
    dag=dag,
    mounts=[Mount(source="\\\\wsl.localhost\\Ubuntu\\opt\\grass\\grassdata", target="/grassdb", type="bind")],
)


mask = DockerOperator(
    task_id='grass_docker_task_mask',
    #image='hello-world',
    image='mundialis/grass-py3-pdal:8.2.1-alpine',
    api_version='auto',
    auto_remove=True,
    docker_url=f'tcp://host.docker.internal:2375',
    mount_tmp_dir=False,
    command='grass /grassdb/test/PERMANENT --exec bash /grassdb/scripts/mask.sh ',
    dag=dag,
    mounts=[Mount(source="\\\\wsl.localhost\\Ubuntu\\opt\\grass\\grassdata", target="/grassdb", type="bind")],
)


ndvi >> buffer >> mask