import boto3

iam = boto3.resource("iam")

res = iam.meta.client.delete_access_key(
    UserName='Surendraku_mar',
    AccessKeyId='AKIAY4LZQRGISPQD23NG'
)

print(res)
