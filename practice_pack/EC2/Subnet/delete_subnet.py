
import boto3

ec2 = boto3.resource('ec2')

response = ec2.meta.client.delete_subnet(
    SubnetId='subnet-0d03b6147d409826a'
)