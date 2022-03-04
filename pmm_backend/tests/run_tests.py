from pmm_backend import api
from pmm_backend.tests.test_user import TestUser
from pmm_backend.tests.test_login import TestLogin
from pmm_backend.tests.test_team import TestTeam

client = api.test_client()

#######
# Login
#######
print("Testing Login")
admin_token = TestLogin.test_admin_login(client)
user_token = TestLogin.test_user_login(client)

TestLogin.test_invalid_password_login(client)
TestLogin.test_invalid_mail_login(client)
TestLogin.test_missing_mail_login(client)

#######
# Users
#######
print("Testing Users")

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


#######
# Teams
#######
print("Testing Teams")

team_id = TestTeam.test_add_and_list_team(client, admin_token)
TestTeam.test_edit_and_list_team(client, admin_token, team_id)
TestTeam.test_remove_team(client, admin_token, team_id)

TestTeam.test_add_team_missing_name(client, admin_token)
TestTeam.test_add_team_missing_description(client, admin_token)
TestTeam.test_remove_invalid_team(client, admin_token)
TestTeam.test_update_invalid_team(client, admin_token)
