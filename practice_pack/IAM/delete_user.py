import boto3

iam = boto3.resource("iam")
response = iam.meta.client.delete_user(
    UserName='surendra_kumar123'
)