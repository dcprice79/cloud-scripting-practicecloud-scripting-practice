import boto3
# create an IAM client
iam = boto3.client('iam')

#Get list of IAM users
response = iam.list_users()

#Print header 
print("IAM Users in your AWS account:")
print("-" *40)

#Loop through each user and print details 
for user in response['Users']:
    print(f"Username: {user['UserName']}")
    print(f"User ID: {user['UserId']}")
    print(f"Created: {user['CreateDate']}")
    print("-" * 40)

#Print total count 
print(f"Total users: {len(response['Users'])}")
