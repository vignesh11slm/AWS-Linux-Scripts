import boto3
import pandas as pd

# Set up connection parameters
database_name = 'mydb'
db_cluster_arn = 'arn:aws:redshift:us-east-1:123456789012:cluster:mycluster'
db_credentials_secrets_store_arn = 'arn:aws:secretsmanager:us-east-1:123456789012:secret:myredshiftsecret'
table_name = 'mytable'

# Set up the SQL query to retrieve data from the table
sql = f"SELECT * FROM {table_name}"

# Set up the Redshift Data API client
client = boto3.client('redshift-data')

# Execute the SQL statement using the Data API
response = client.execute_statement(
    ClusterIdentifier=db_cluster_arn,
    Database=database_name,
    DbUser='myuser',
    Sql=sql,
    SecretArn=db_credentials_secrets_store_arn
)

# Get the column names from the result set metadata
column_metadata = response['ColumnMetadata']
column_names = [column['name'] for column in column_metadata]

# Get the data from the result set
records = response['Records']
data = [[record['stringValue'] if 'stringValue' in record else None for record in records]]
    
# Create a Pandas DataFrame from the data
df = pd.DataFrame(data, columns=column_names)
