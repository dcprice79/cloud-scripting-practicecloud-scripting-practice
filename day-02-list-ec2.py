import boto3

ec2 = boto3.client('ec2' , region_name='us-east-1')
response = ec2.describe_instances(
  Filters=[ { 'Name': 'instance-state-name', 'Values': ['running']}]
)

for reservation in response['Reservations']:
  for instance in reservation['Instance']:
        print(f"Instance: {instance['InstanceId']} | Type: {instance['InstanceType']} | State: {instance['State']['Name']}")
    

  
