from pmm_backend import api
from pmm_backend.tests.test_user import TestUser

client = api.test_client()
token = TestUser.test_login(client)

#######
# Users
#######

user_id = TestUser.test_add_and_list_user(client, token)
TestUser.test_remove_user(client, token, user_id)

TestUser.test_add_user_missing_email(client, token)