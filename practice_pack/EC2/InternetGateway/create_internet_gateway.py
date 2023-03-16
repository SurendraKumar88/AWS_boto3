import boto3
ec2 = boto3.resource('ec2')

response = ec2.meta.client.create_internet_gateway()

print(response)