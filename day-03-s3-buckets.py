import boto3

s3 = boto3.client('s3')
response = s3.list_buckets()

print(f"You have {len(response['Buckets'])} S3 buckets")
for bucket in response['Buckets']:
  print(f" {bucket['Name']} - created {bucket['CreationDate']}")
