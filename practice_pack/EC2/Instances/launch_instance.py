from datetime import datetime

import boto3
ec2 = boto3.resource("ec2")

response = ec2.create_instances(
        ImageId="ami-0d81306eddc614a45",
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",
        KeyName="demo-vpc"
)

print(response)