"""
Airflow DAG to trigger Databricks Serverless Job
co2 Emissions ETL: Bronze → Silver → Gold
"""

from airflow import DAG
from airflow.providers.databricks.operators.databricks import DatabricksRunNowOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "Gayathri",
    "depends_on_past": False,
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="stock_analysis",
    description="Trigger Databricks Serverless Job for stock analysis",
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,   
    catchup=False,
    tags=["stock", "databricks", "serverless"],
) as dag:

    run_superstore_job = DatabricksRunNowOperator(
        task_id="run_stock_analysis_serverless_job",
        databricks_conn_id="databricks_default",
        job_id=558961576002013  
    )