import kagglehub
import pandas as pd

# Download latest version
# sales = kagglehub.dataset_download("kyanyoga/sample-sales-data")

# ecommerce = kagglehub.dataset_download("carrie1/ecommerce-data")

# customer = kagglehub.dataset_download("kaushiksuresh147/customer-segmentation")

# print("Path to dataset sales:", sales)

def extract_sales():
    return pd.read_csv('data/raw/sales.csv')

def extract_customers():
    return pd.read_csv('data/raw/customers.csv')

def extract_products():
    return pd.read_csv('data/raw/products.csv')

