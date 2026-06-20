from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    "owner": "airflow",
    "start_date": datetime(2024, 1, 1),
    "retries": 1,
}

with DAG(
    dag_id="dbt_run_test_model_only",
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
) as dag:

    dbt_run = BashOperator(
        task_id="run_test_model",
        bash_command="dbt run --select test_model",
        cwd="/opt/airflow/dbt"   # ✅ No need for cd
    )
