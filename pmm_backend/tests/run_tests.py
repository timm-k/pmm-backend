from pmm_backend import api
from pmm_backend.tests.test_user import TestUser
from pmm_backend.tests.test_login import TestLogin

client = api.test_client()

#######
# Login
#######

admin_token = TestLogin.test_admin_login(client)
user_token = TestLogin.test_user_login(client)

TestLogin.test_invalid_password_login(client)
TestLogin.test_invalid_mail_login(client)
TestLogin.test_missing_mail_login(client)

#######
# Users
#######


user_id = TestUser.test_add_and_list_user(client, admin_token)
TestUser.test_edit_and_list_user(client, admin_token, user_id)
TestUser.test_remove_user(client, admin_token, user_id)

TestUser.test_add_user_missing_email(client, admin_token)
TestUser.test_remove_invalid_user(client, admin_token)
TestUser.test_update_invalid_user(client, admin_token)

TestUser.test_add_user_invalid_token(client)
TestUser.test_add_user_missing_token(client)
TestUser.test_list_user_invalid_token(client)
TestUser.test_list_user_missing_token(client)
