import json

class TestTeam:
    @staticmethod
    def test_add_and_list_team(client, token):
        data = {"name": "test_team",
                "description": "test_team_description"}

        response = client.post("/team", data=data, headers={"x-access-token": token})
        team_id = response.json["team_id"]
        assert response.status_code == 200
        assert response.json["message"] == "success"

        response = client.get("/team/list", headers={"x-access-token": token})
        assert response.status_code == 200

        user_list = json.loads(response.data)
        for u in user_list:
            if int(team_id) == int(u['team_id']):
                assert u['first_name'] == "test_first_name"
                assert u['role_id'] == 1

        return team_id
    
    
    
    @staticmethod
    def test_edit_and_list_team(client, token, team_id):
        data = {"name": "test_team_edit",
                "description": "test_team_description_edit"}

        response = client.put("/team/" + str(team_id), data=data, headers={"x-access-token": token})
        assert response.status_code == 200
        assert response.json["message"] == "success"

        response = client.get("/team/list", headers={"x-access-token": token})
        assert response.status_code == 200

        team_list = json.loads(response.data)
        for t in team_list:
            if int(team_id) == int(t['team_id']):
                assert t['first_name'] == "test_edited_first_name"
                assert t['role_id'] == 2


    @staticmethod
    def test_remove_user(client, token, team_id):
        response = client.delete("/user/" + str(team_id), headers={"x-access-token": token})
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

    @staticmethod
    def test_add_user_invalid_token(client):
        data = {"email": "test_user@test.com",
                "password": "test",
                "first_name": "test_first_name",
                "last_name": "test_last_name",
                "role_id": 1}

        response = client.post("/user", data=data, headers={"x-access-token": "SDsdjkl"})
        assert response.status_code == 401

    @staticmethod
    def test_add_user_missing_token(client):
        data = {"email": "test_user@test.com",
                "password": "test",
                "first_name": "test_first_name",
                "last_name": "test_last_name",
                "role_id": 1}

        response = client.post("/user", data=data)
        assert response.status_code == 401

    @staticmethod
    def test_list_user_invalid_token(client):
        response = client.get("/user/list", headers={"x-access-token": "fjskljdl"})
        assert response.status_code == 401

    @staticmethod
    def test_list_user_missing_token(client):
        response = client.get("/user/list")
        assert response.status_code == 401