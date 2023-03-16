import boto3

iam = boto3.resource("iam")

response = iam.meta.client.update_user(
    UserName='Surendrakumar',
    NewUserName='surendra_kumar123'
)

print(response)