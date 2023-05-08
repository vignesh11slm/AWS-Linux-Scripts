import boto3
import pandas as pd

# create a connection to S3
s3 = boto3.client('s3')

# specify the bucket name and file name
bucket_name = 'your_bucket_name'
file_name = 'your_file_name.csv'

# read the file from S3 using pandas
s3_object = s3.get_object(Bucket=bucket_name, Key=file_name)
df = pd.read_csv(s3_object['Body'])

# get the number of columns in the dataframe
num_cols = len(df.columns)

# print the number of columns
print(f"The file '{file_name}' has {num_cols} columns.")
