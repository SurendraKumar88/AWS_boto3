import boto3

#Using paginator
client = boto3.client("iam")

paginator = client.get_paginator('list_access_keys')
pagi = paginator.paginate()
for keys in pagi:
    for key in keys['AccessKeyMetadata']:
        print(key['AccessKeyId'])