class TestLogin:
    @staticmethod
    def test_admin_login(client):
        response = client.post("/user/login",  data={"email": "test@test.com", "password": "ABC"})
        assert response.status_code == 200
        assert response.json["message"] == "success"

        return response.json["token"]

    @staticmethod
    def test_user_login(client):
        response = client.post("/user/login",  data={"email": "testuser@test.com", "password": "ABC"})
        assert response.status_code == 200
        assert response.json["message"] == "success"

        return response.json["token"]

    @staticmethod
    def test_invalid_password_login(client):
        response = client.post("/user/login", data={"email": "test@test.com", "password": "SDfjkljsd"})
        assert response.status_code == 401
        assert "invalid password" in response.json["message"]

    @staticmethod
    def test_invalid_mail_login(client):
        response = client.post("/user/login", data={"email": "aslfjsfd@dfjagkldf.com", "password": "SDfjkljsd"})
        assert response.status_code == 401
        assert "invalid login" in response.json["message"]

    @staticmethod
    def test_missing_mail_login(client):
        response = client.post("/user/login", data={"password": "SDfjkljsd"})
        assert response.status_code == 401
        assert "invalid login" in response.json["message"]