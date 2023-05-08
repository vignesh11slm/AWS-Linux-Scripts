import boto3
import gzip
import io

# Set up the S3 client
s3 = boto3.client("s3")

# Define the source and destination folders in S3
src_bucket = "source-bucket"
src_prefix = "source-folder/"
dest_bucket = "destination-bucket"
dest_prefix = "destination-folder/"

# Get a list of all the files in the source S3 folder
response = s3.list_objects_v2(Bucket=src_bucket, Prefix=src_prefix)
files = [obj["Key"] for obj in response.get("Contents", [])]

# Iterate over each file and archive it in gzip format
for file in files:
    # Get the object data from S3
    obj = s3.get_object(Bucket=src_bucket, Key=file)
    data = obj["Body"].read()
    
    # Compress the data using gzip
    compressed_data = io.BytesIO()
    with gzip.GzipFile(fileobj=compressed_data, mode="wb") as gz:
        gz.write(data)
    compressed_data.seek(0)
    
    # Upload the compressed data to the destination S3 folder
    dest_file = file.replace(src_prefix, dest_prefix)
    s3.put_object(Bucket=dest_bucket, Key=dest_file, Body=compressed_data.read())
