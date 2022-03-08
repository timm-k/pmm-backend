from pmm_backend import api
from pmm_backend.tests.test_user import TestUser
from pmm_backend.tests.test_login import TestLogin
from pmm_backend.tests.test_team import TestTeam
from pmm_backend.tests.test_team_role import TestTeamRole
from pmm_backend.tests.test_employee import TestEmployee
from pmm_backend.tests.test_project import TestProject
from pmm_backend.tests.test_work_package import TestWorkPackage

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


#######
# Teams
#######

team_id = TestTeam.test_add_and_list_team(client, admin_token)
TestTeam.test_edit_and_list_team(client, admin_token, team_id)
TestTeam.test_remove_team(client, admin_token, team_id)

TestTeam.test_add_team_missing_name(client, admin_token)
TestTeam.test_add_team_missing_description(client, admin_token)
TestTeam.test_remove_invalid_team(client, admin_token)
TestTeam.test_update_invalid_team(client, admin_token)


#######
# Team Roles
#######

team_role_id = TestTeamRole.test_add_and_list_team_role(client, admin_token)
TestTeamRole.test_edit_and_list_team_role(client, admin_token, team_role_id)
TestTeamRole.test_remove_team_role(client, admin_token, team_role_id)

TestTeamRole.test_add_team_role_missing_name(client, admin_token)
TestTeamRole.test_add_team_role_missing_description(client, admin_token)
TestTeamRole.test_remove_invalid_team_role(client, admin_token)
TestTeamRole.test_update_invalid_team_role(client, admin_token)

#######
# Employees
#######

employee_id = TestEmployee.test_add_and_list_employee(client, admin_token)
TestEmployee.test_edit_and_list_employee(client, admin_token, employee_id)
TestEmployee.test_remove_employee(client, admin_token, employee_id)

TestEmployee.test_add_employee_missing_first_name(client, admin_token)
TestEmployee.test_add_employee_missing_last_name(client, admin_token)
TestEmployee.test_remove_invalid_employee(client, admin_token)
TestEmployee.test_update_invalid_employee(client, admin_token)

#######
# Projects
#######

project_id = TestProject.test_add_and_list_project(client, admin_token)
TestProject.test_edit_and_list_project(client, admin_token, project_id)

TestProject.test_add_project_missing_name(client, admin_token)
TestProject.test_add_project_missing_description(client, admin_token)
TestProject.test_add_project_missing_timestamps(client, admin_token)
TestProject.test_remove_invalid_project(client, admin_token)
TestProject.test_update_invalid_project(client, admin_token)

#######
# Work Packages
#######

work_package_id = TestWorkPackage.test_add_and_list_work_package(client, admin_token, project_id)
TestWorkPackage.test_edit_and_list_work_package(client, admin_token, work_package_id, project_id)
TestWorkPackage.test_remove_work_package(client, admin_token, work_package_id)

TestWorkPackage.test_add_work_package_missing_name(client, admin_token, project_id)
TestWorkPackage.test_add_work_package_missing_description(client, admin_token, project_id)
TestWorkPackage.test_add_work_package_missing_project_id(client, admin_token)
TestWorkPackage.test_add_work_package_missing_timestamps(client, admin_token, project_id)
TestWorkPackage.test_remove_invalid_work_package(client, admin_token)
TestWorkPackage.test_update_invalid_work_package(client, admin_token)
TestWorkPackage.test_add_work_package_invlalid_project_id(client, admin_token)


####
# Sonstiges
####

TestProject.test_remove_project(client, admin_token, project_id)
