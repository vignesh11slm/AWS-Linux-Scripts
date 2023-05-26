

1. Extract schema for a table:

```
aws redshift describe-table --cluster-identifier <cluster-identifier> --database-name <database-name> --table-name <table-name> --query 'Table.Columns[*].[Name,Type]' --output text
```

Replace `<cluster-identifier>`, `<database-name>` and `<table-name>` with the actual values for your Redshift cluster, database and table.

2. Retrieve count of rows in each table from a table list:

```
for table_name in <table1> <table2> <table3>; do
    echo "$table_name"
    aws redshift describe-table --cluster-identifier <cluster-identifier> --database-name <database-name> --table-name "$table_name" --query 'Table.TableRowCount' --output text
done
```

Replace `<cluster-identifier>`, `<database-name>` and `<table1>`, `<table2>`, `<table3>` with the actual values for your Redshift cluster, database and tables.

3. Truncate the tables from a list:

```
for table_name in <table1> <table2> <table3>; do
    aws redshift execute-statement --cluster-identifier <cluster-identifier> --database <database-name> --sql "TRUNCATE TABLE $table_name;"
done
```

Replace `<cluster-identifier>`, `<database-name>` and `<table1>`, `<table2>`, `<table3>` with the actual values for your Redshift cluster, database and tables.

4. Output table sample records:

```
aws redshift execute-statement --cluster-identifier <cluster-identifier> --database-name <database-name> --sql "SELECT * FROM <table-name> LIMIT 10" --output text
```

Replace `<cluster-identifier>`, `<database-name>` and `<table-name>` with the actual values for your Redshift cluster, database and table. The `LIMIT` clause in the SQL query can be adjusted to return more or fewer rows.

5. List of Step Functions:
```
aws stepfunctions list-state-machines --query "stateMachines[].name" --output text
```

6. Execute a Step Function:
```
aws stepfunctions start-execution --state-machine-arn <STATE_MACHINE_ARN> --input '{ "key1": "value1", "key2": "value2" }'
```
Note: Replace `<STATE_MACHINE_ARN>` with the actual ARN of the Step Function to execute, and update the input payload as needed.

7. List of Glue Jobs:
```
aws glue get-jobs --query "Jobs[].Name" --output text
```

8. Execute a Glue Job:
```
aws glue start-job-run --job-name <GLUE_JOB_NAME>
```
Note: Replace `<GLUE_JOB_NAME>` with the actual name of the Glue Job to execute.