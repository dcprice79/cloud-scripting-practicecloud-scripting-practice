import boto3

# Create a CloudWatch client
cloudwatch = boto3.client('cloudwatch')

# Get list of all alarms 
response = cloudwatch.describe_alarms()

# Print header 
print("CloudWatch Alarms in you AWS account:")
print("-" * 40)

#Loop through each alarm and print details 
for alarm in response['MetricAlarms']:
    print(f"AlarmName: {alarm['AlarmName']}")
    print(f"State: {alarm['StateValue']}")
    print(f"Description: {alarm.get('AlarmDescription' , 'No description')}")
    print("-" * 40)

#Print total count 
print(f"Total alarms: {len(response['MetricAlarms'])}")
