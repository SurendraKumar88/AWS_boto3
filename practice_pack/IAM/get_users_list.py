import boto3

#using client - will get only one page data, will not get data in all pages
iam = boto3.resource("iam")
for user in iam.meta.client.list_users()['Users']:
    print(user['UserName'])


#Using Paginator - will get data in all pages
'''

client = boto3.client("iam")

paginator = client.get_paginator('list_users')

pagi = paginator.paginate()
for users in pagi:
    for user in users['Users']:
        print(user['UserName'])
        
'''
