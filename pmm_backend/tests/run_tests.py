from pmm_backend import api
from pmm_backend.tests.test_user import TestUser

client = api.test_client()

token = TestUser.test_login(client)
TestUser.test_add_and_list_user(client, token)