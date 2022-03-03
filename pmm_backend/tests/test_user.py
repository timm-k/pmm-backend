import json

class TestUser:
    @staticmethod
    def test_add_and_list_user(client, token):
        data = {"email": "test_user@test.com",
                "password": "test",
                "first_name": "test_first_name",
                "last_name": "test_last_name",
                "role_id": 1}

        response = client.post("/user", data=data, headers={"x-access-token": token})
        user_id = response.json["user_id"]
        assert response.status_code == 200
        assert response.json["message"] == "success"

        response = client.get("/user/list", headers={"x-access-token": token})
        assert response.status_code == 200

        user_list = json.loads(response.data)
        for u in user_list:
            if int(user_id) == int(u['user_id']):
                assert u['first_name'] == "test_first_name"
                assert u['role_id'] == 1

        return user_id

    @staticmethod
    def test_edit_and_list_user(client, token, user_id):
        data = {"email": "test_user@test.com",
                "password": "test",
                "first_name": "test_edited_first_name",
                "last_name": "test_edited_last_name",
                "role_id": 2}

        response = client.put("/user/" + str(user_id), data=data, headers={"x-access-token": token})
        assert response.status_code == 200
        assert response.json["message"] == "success"

        response = client.get("/user/list", headers={"x-access-token": token})
        assert response.status_code == 200

        user_list = json.loads(response.data)
        for u in user_list:
            if int(user_id) == int(u['user_id']):
                assert u['first_name'] == "test_edited_first_name"
                assert u['role_id'] == 2


    @staticmethod
    def test_remove_user(client, token, user_id):
        response = client.delete("/user/" + str(user_id), headers={"x-access-token": token})
        assert response.status_code == 200
        assert response.json["message"] == "success"

    @staticmethod
    def test_add_user_missing_email(client, token):
        data = {"password": "test",
                "first_name": "test_first_name",
                "last_name": "test_last_name",
                "role_id": 1}

        response = client.post("/user", data=data, headers={"x-access-token": token})
        assert response.status_code == 400
        assert "missing data" in response.json["message"]

    @staticmethod
    def test_remove_invalid_user(client, token):
        response = client.delete("/user/9999999", headers={"x-access-token": token})
        assert response.status_code == 404
        assert "user not found" in response.json["message"]

    @staticmethod
    def test_update_invalid_user(client, token):
        data = {"email": "test23432@test.com"}

        response = client.put("/user/999999", data=data, headers={"x-access-token": token})
        assert response.status_code == 404
        assert "user not found" in response.json["message"]