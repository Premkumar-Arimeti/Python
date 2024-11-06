import pandas as pd

#load data from csv
data=pd.read_csv("manufacturing_data.csv")
#To calculate average quality score
average_quality_score = data["quality_score"].mean()
print(f"Average Quality Score: {average_quality_score}")
#import boto3
#from pyathena import connect
#query=SELECT product_id, quality_score, test_date 
# FROM database.table
#data=pd.read_sql(query,athena)
