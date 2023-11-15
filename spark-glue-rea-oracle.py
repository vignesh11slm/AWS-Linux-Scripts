from pyspark.context import SparkContext
from pyspark.sql import SparkSession
from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame

# Initialize Spark and Glue contexts
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Define the Oracle connection options
oracle_connection_options = {
    "url": "jdbc:oracle:thin:@//your_oracle_host:your_oracle_port/your_oracle_sid",
    "dbtable": "your_table_name",
    "user": "your_username",
    "password": "your_password",
    "driver": "oracle.jdbc.driver.OracleDriver"
}

# Read data from Oracle database
oracle_dynamic_frame = glueContext.create_dynamic_frame.from_catalog(
    database="your_catalog_name",
    table_name="your_table_name",
    transformation_ctx="oracle_data",
    additional_options=oracle_connection_options
)

# Convert the DynamicFrame to a Spark DataFrame
oracle_data_frame = oracle_dynamic_frame.toDF()

# Perform any necessary transformations if needed

# Define the S3 output path
s3_output_path = "s3://your-s3-bucket/your-output-path/"

# Write the data to S3
oracle_data_frame.write.parquet(s3_output_path)

# Job completion message
print("Job completed successfully!")
