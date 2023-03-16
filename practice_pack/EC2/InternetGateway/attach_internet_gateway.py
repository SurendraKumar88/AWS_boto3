import boto3

ec2 = boto3.resource('ec2')

response = ec2.meta.client.attach_internet_gateway(
    InternetGatewayId='igw-08823a78f38de9ee2',
    VpcId='vpc-08eb5c126910a467c'
)

print(response)