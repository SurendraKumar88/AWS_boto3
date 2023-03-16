import boto3

ec2 = boto3.resource('ec2')

response = ec2.meta.client.create_route_table(
    VpcId='vpc-0a2255c9ac47c5a91'
)

print(response)