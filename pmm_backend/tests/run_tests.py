from pmm_backend import api
from pmm_backend.tests.test_user import TestUser

client = api.test_client()

TestUser.test_login(client)