import boto3

ec2 = boto3.resource('ec2')

response = ec2.meta.client.create_vpc(

    CidrBlock='10.0.0.0/16',
    AmazonProvidedIpv6CidrBlock=False,
    InstanceTenancy='default'

)

print(response)




