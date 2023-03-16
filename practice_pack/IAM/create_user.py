import boto3

iam = boto3.resource("iam")
create_user = iam.meta.client.create_user(UserName="Surendraku_mar",)
print(create_user)



