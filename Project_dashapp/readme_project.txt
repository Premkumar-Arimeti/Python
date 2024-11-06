created a .csv file
product_id,quality_score,test_date
1001,85,2024-11-01
1002,92,2024-11-02
1003,88,2024-11-03

pip install pandas boto3 PyAthena dash

if needed add correct environment path

#Loading and data manipulating with pandas
import pandas as pd

#connect to amazon s3 and Athena
import boto3
from pyathena import connect
# Initialize S3 and Athena clients
s3 = boto3.client('s3')
athena = connect(s3_staging_dir="s3://your-athena-staging-bucket/",
                 region_name="your-region")

# Query Athena for data
query = """
SELECT product_id, quality_score, test_date
FROM your_database.your_table
"""
data = pd.read_sql(query, athena)


#create dash app
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px