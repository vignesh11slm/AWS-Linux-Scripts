import boto3

# Set up connection parameters
dbname = 'mydb'
cluster_id = 'mycluster'
database_user = 'myuser'
sql = "INSERT INTO mytable (column1, column2, column3) VALUES ('value1', 'value2', 'value3')"

# Set up a Redshift Data API client
client = boto3.client('redshift-data')

# Execute the SQL statement using the Redshift Data API
response = client.execute_statement(Database=dbname, ClusterIdentifier=cluster_id, DbUser=database_user, Sql=sql)
