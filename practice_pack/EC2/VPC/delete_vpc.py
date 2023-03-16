import boto3

ec2 = boto3.resource("ec2")

response = ec2.meta.client.delete_vpc(
    VpcId='vpc-097643f3215a6f101'

)

print(response)