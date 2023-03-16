import boto3


class TestIamUsers:
    iam = boto3.resource("iam")
    user_name = "Surendrakumar"
    update_username = "Surendra_kumar123"
    accessKeyId = ""

    def test_create_user(self):
        response = self.iam.meta.client.create_user(
            UserName=self.user_name
        )
        print("Response:", response)
        user = response['User']['UserName']
        assert user == self.user_name

    def test_create_access_key(self):
        response = self.iam.meta.client.create_access_key(
            UserName=self.user_name
        )
        print("Response:", response)

        response_data = response['AccessKey']
        user = response_data['UserName']
        TestIamUsers.accessKeyId = response_data['AccessKeyId']
        secretAccessKey = response_data['SecretAccessKey']

        print("AccessKeyId", TestIamUsers.accessKeyId)
        print("SecretAccessKey", secretAccessKey)

        assert user == self.user_name
        assert "" != TestIamUsers.accessKeyId, "AccessKeyId not generated"
        assert "" != secretAccessKey, "SecretAccessKey not generated"

    def test_delete_access_key(self):
        response = self.iam.meta.client.delete_access_key(
            UserName=self.user_name,
            AccessKeyId=TestIamUsers.accessKeyId
        )
        print("Response:", response)
        status_code = response['ResponseMetadata']['HTTPStatusCode']
        assert status_code == 200

    def test_get_list_users(self):
        response = self.iam.meta.client.list_users()
        print("Response:", response)
        users = response['Users']

        users_list = []
        for user in users:
            users_list.append(user['UserName'])
        print("Users_lists:", users_list)

        res = False
        if self.user_name in users_list:
            res = True
        assert res, "{} not available in user list. these are the user list: {}".format(self.user_name, users_list)

    def test_update_user(self):
        response = self.iam.meta.client.update_user(
            UserName=self.user_name,
            NewUserName=self.update_username
        )
        print("Response:", response)
        status_code = response['ResponseMetadata']['HTTPStatusCode']
        assert status_code == 200

    def test_delete_user(self):
        response = self.iam.meta.client.delete_user(
            UserName=self.update_username
        )
        print("Response:", response)
        status_code = response['ResponseMetadata']['HTTPStatusCode']
        assert status_code == 200