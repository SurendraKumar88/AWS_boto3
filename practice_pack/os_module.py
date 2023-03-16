import os

#res = list(os.walk("/Users/surendrakumar/PycharmProjects/AWS_boto3"))
#print(res)

for dirname, dirpath, filename in os.walk("/Users/surendrakumar/PycharmProjects/AWS_boto3"):
    print(dirname)
    print(dirpath)
    print(filename)
    print("**********")

