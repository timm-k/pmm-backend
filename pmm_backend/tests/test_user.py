class TestUser:
    @staticmethod
    def test_login(client):
        response = client.post("/user/login",  data={"email": "test@test.com", "password": "ABC"})
        assert response.status_code == 201
        assert response.json["message"] == "success"

        return response.json["token"]

    @staticmethod
    def test_add_and_list_user(client, token):
        data = {"email": "test_user@test.com",
                "password": "test",
                "first_name": "test_first_name",
                "last_name": "test_last_name",
                "role_id": 1}
        client.post("/user", data=data, headers={"x-access-token": token})
        client.get("/user/list", headers={"x-access-token": token})
