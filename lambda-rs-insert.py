import boto3
import json

def lambda_handler(event, context):
    # Replace these values with your own Redshift cluster details
    cluster_identifier = 'your-redshift-cluster-identifier'
    database_name = 'your-database-name'
    db_user = 'your-database-username'
    secret_arn = 'your-secret-arn'
    table_name = 'your-table-name'

    # Replace this with your actual record data
    record_data = {
        'column1': 'value1',
        'column2': 'value2',
        # Add more columns and values as needed
    }

    # Create a Redshift Data API client
    client = boto3.client('redshift-data')

    # Prepare the SQL statement to insert a record
    sql_statement = f"INSERT INTO {table_name} ({', '.join(record_data.keys())}) VALUES ({', '.join([':' + key for key in record_data.keys()])})"

    # Execute the SQL statement with the record data
    response = client.execute_statement(
        ClusterIdentifier=cluster_identifier,
        Database=database_name,
        DbUser=db_user,
        SecretArn=secret_arn,
        Sql=sql_statement,
        Parameters=[{'name': key, 'value': {'stringValue': str(value)}} for key, value in record_data.items()]
    )

    # Check the execution status
    if response['status'] == 'FINISHED':
        return {
            'statusCode': 200,
            'body': json.dumps('Record inserted successfully!')
        }
    else:
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error inserting record. Status: {response['status']}")
        }
