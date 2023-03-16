import boto3

ec2 = boto3.resource('ec2')

response = ec2.meta.client.delete_route_table(
    RouteTableId='rtb-0cc211fc97da1ab78',
)

print(response)