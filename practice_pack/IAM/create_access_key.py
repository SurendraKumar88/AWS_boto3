import boto3

iam = boto3.resource("iam")

create_access_key_for_user = iam.meta.client.create_access_key(UserName="Surendraku_mar")["AccessKey"]
print("UserName:", create_access_key_for_user['UserName'])
print("AccessKeyId:", create_access_key_for_user['AccessKeyId'])
print("SecretAccessKey:", create_access_key_for_user['SecretAccessKey'])



