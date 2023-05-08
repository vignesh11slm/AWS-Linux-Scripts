import boto3
import sys

# Set up the S3 client
s3 = boto3.client("s3")

# Define the source and destination folders in S3
src_bucket = "source-bucket"
src_prefix = "source-folder/"
failed_bucket = "failed-bucket"
failed_prefix = "failed-folder/"

# Get a list of all the files in the source S3 folder
response = s3.list_objects_v2(Bucket=src_bucket, Prefix=src_prefix)
files = [obj["Key"] for obj in response.get("Contents", [])]

# Iterate over each file and check if it is empty
for file in files:
    # Get the object data from S3
    obj = s3.get_object(Bucket=src_bucket, Key=file)
    data = obj["Body"].read().decode("utf-8")
    
    # Check if the data is empty
    if len(data.strip()) == 0:
        print(f"{file} is empty, moving to failed folder")
        
        # Move the file to the failed folder
        failed_file = file.replace(src_prefix, failed_prefix)
        s3.copy_object(Bucket=failed_bucket, CopySource={"Bucket": src_bucket, "Key": file}, Key=failed_file)
        s3.delete_object(Bucket=src_bucket, Key=file)
    else:
        print(f"{file} is not empty, processing...")
