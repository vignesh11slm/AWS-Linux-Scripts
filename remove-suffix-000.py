import boto3
import os
import gzip

s3_client = boto3.client('s3')
bucket_name = 'your_bucket_name'  # Replace with your S3 bucket name
folder_path = 'your_folder_path'  # Replace with the path to the folder containing the CSV files in the bucket

response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=folder_path)

# Iterate over the objects in the bucket
for obj in response['Contents']:
    file_key = obj['Key']

    # Check if the object is a CSV file
    if file_key.endswith('.csv000'):
        # Remove the '000' suffix from the file name
        file_name = os.path.basename(file_key)
        new_file_name = file_name[:-3] if file_name.endswith('000') else file_name

        # Copy the object with a new key to remove the suffix
        new_file_key = folder_path + new_file_name
        s3_client.copy_object(Bucket=bucket_name, CopySource={'Bucket': bucket_name, 'Key': file_key},
                              Key=new_file_key)

        # Read the CSV file content
        response = s3_client.get_object(Bucket=bucket_name, Key=new_file_key)
        csv_content = response['Body'].read()

        # Gzip the file content
        gzipped_content = gzip.compress(csv_content)

        # Upload the gzipped file content to S3
        gzipped_file_key = new_file_key + '.gz'
        s3_client.put_object(Bucket=bucket_name, Key=gzipped_file_key, Body=gzipped_content)

        # Remove the original CSV file
        s3_client.delete_object(Bucket=bucket_name, Key=file_key)
