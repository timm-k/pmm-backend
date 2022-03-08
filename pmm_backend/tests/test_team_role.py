import json


class TestTeamRole:
    @staticmethod
    def test_add_and_list_team_role(client, token):
        data = {"name": "test_team_role",
                "description": "test_team_role_description"}

        response = client.post("/team/role", data=data, headers={"x-access-token": token})
        team_role_id = response.json["team_role_id"]
        assert response.status_code == 200
        assert response.json["message"] == "success"

        response = client.get("/team/role/list", headers={"x-access-token": token})
        assert response.status_code == 200

        user_list = json.loads(response.data)
        for u in user_list:
            if int(team_role_id) == int(u['team_role_id']):
                assert u['name'] == "test_team_role"
                assert u['description'] == "test_team_role_description"

        return team_role_id

    @staticmethod
    def test_edit_and_list_team_role(client, token, team_role_id):
        data = {"name": "test_team_role_edit",
                "description": "test_team_role_description_edit"}

        response = client.put("/team/role/" + str(team_role_id), data=data, headers={"x-access-token": token})
        assert response.status_code == 200
        assert response.json["message"] == "success"

        response = client.get("/team/role/list", headers={"x-access-token": token})
        assert response.status_code == 200

        team_list = json.loads(response.data)
        for t in team_list:
            if int(team_role_id) == int(t['team_role_id']):
                assert t['name'] == "test_team_role_edit"
                assert t['description'] == "test_team_role_description_edit"

    @staticmethod
    def test_remove_team_role(client, token, team_role_id):
        response = client.delete("/team/role/" + str(team_role_id), headers={"x-access-token": token})
        assert response.status_code == 200
        assert response.json["message"] == "success"

    @staticmethod
    def test_add_team_role_missing_name(client, token):
        data = {"description": "test"}

        response = client.post("/team/role", data=data, headers={"x-access-token": token})
        assert response.status_code == 400
        assert "missing data" in response.json["message"]

    @staticmethod
    def test_add_team_role_missing_description(client, token):
        data = {"name": "test"}

        response = client.post("/team/role", data=data, headers={"x-access-token": token})
        assert response.status_code == 400
        assert "missing data" in response.json["message"]

    @staticmethod
    def test_remove_invalid_team_role(client, token):
        response = client.delete("/team/role/9999999", headers={"x-access-token": token})
        assert response.status_code == 404
        assert "team role not found" in response.json["message"]

    @staticmethod
    def test_update_invalid_team_role(client, token):
        data = {"name": "test234"}

        response = client.put("/team/role/999999", data=data, headers={"x-access-token": token})
        assert response.status_code == 404
        assert "team role not found" in response.json["message"]

