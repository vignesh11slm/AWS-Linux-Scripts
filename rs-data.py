import boto3
import time
import json

# Create a Redshift Data API client
redshift_data_api_client = boto3.client('redshift-data')

# Create a Secrets Manager client
secrets_manager_client = boto3.client('secretsmanager')

# Define your cluster identifier, database name, and SQL command
cluster_id = 'your-cluster-id'
database = 'your-database'
sql_command = 'SELECT * FROM your_table'

# Get the database credentials from Secrets Manager
secret_name = 'your-secret-name'
response = secrets_manager_client.get_secret_value(SecretId=secret_name)
credentials = json.loads(response['SecretString'])

# Start the execution of the SQL command
response = redshift_data_api_client.execute_statement(
    ClusterIdentifier=cluster_id,
    Database=database,
    DbUser=credentials['username'],
    Sql=sql_command,
    SecretArn=credentials['arn'] # The ARN of the secret that enables access to the DB
)

# Get the SQL command execution ID
id = response['Id']

# Check the status of the SQL command execution
while True:
    details = redshift_data_api_client.describe_statement(Id=id)
    status = details['Status']
    if status == 'FINISHED':
        break
    print('Waiting for SQL command execution to finish...')
    time.sleep(1)  # Delay for 1 second

# Get the result of the SQL command
results = redshift_data_api_client.get_statement_result(Id=id)
for row in results['Records']:
    print(row)
