from pmm_backend import api
from pmm_backend.controllers.user import UserController

@api.route('/users')
def list_users():
    return UserController.list_users()