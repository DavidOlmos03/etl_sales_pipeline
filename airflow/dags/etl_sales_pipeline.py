from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../scripts')))
# sys.path.append('/opt/airflow/scripts')

# from extract import extract_sales, extract_customers, extract_products
# from transform import transform_data
# from load import load_data

default_args = {
    'start_date': datetime(2024, 1, 1),
    'catchup': False
} 

with DAG('etl_sales_pipeline', schedule='@daily', default_args=default_args, tags=['etl'], description='etl pipeline demo', ) as dag:

    def extract():
        global sales, customers, products
        sales = extract_sales()
        customers = extract_customers()
        products = extract_products()

    def transform():
        global transformed_df
        transformed_df = transform_data(sales, customers, products)

    def load():
        load_data(transformed_df)

    t1 = PythonOperator(task_id='extract', python_callable=extract)
    t2 = PythonOperator(task_id='transform', python_callable=transform)
    t3 = PythonOperator(task_id='load', python_callable=load)

    t1 >> t2 >> t3

