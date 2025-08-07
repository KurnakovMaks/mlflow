import os
import boto3

s3 = boto3.client('s3',
                  endpoint_url=os.environ['MLFLOW_S3_ENDPOINT_URL'],
                  aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
                  aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'])

try:
  s3.create_bucket(Bucket=os.environ['BUCKET_NAME'])
  print("Success! Bucket is created")
except Exception as e:
  if "BucketAlreadyOwnedByYou" in str(e):
    print("Bucket already exist")
  else:
    print(f"Error: {e}")