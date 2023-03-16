import  boto3

ec2 = boto3.resource('ec2')

response = ec2.meta.client.describe_vpcs(
VpcIds=[
        'vpc-0f59f52fede110b20',
        'vpc-097643f3215a6f101'
    ]

)

print(response)