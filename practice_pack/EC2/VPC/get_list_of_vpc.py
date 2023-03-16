import  boto3

ec2 = boto3.resource('ec2')

response = ec2.meta.client.describe_vpcs()

for vpc in response['Vpcs']:
    print(vpc['VpcId'])