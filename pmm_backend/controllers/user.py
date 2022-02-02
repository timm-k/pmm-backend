from pmm_backend import api

class UserController():
    @staticmethod
    @api.route('/users')
    def test():
        return "hi"
