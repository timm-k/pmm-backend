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
                assert u['name'] == "test_team"
                assert u['description'] == "test_team_description"

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
                assert t['name'] == "test_team_edit"
                assert t['description'] == "test_team_description_edit"


    @staticmethod
    def test_remove_team(client, token, team_id):
        response = client.delete("/team/" + str(team_id), headers={"x-access-token": token})
        assert response.status_code == 200
        assert response.json["message"] == "success"

    @staticmethod
    def test_add_team_missing_name(client, token):
        data = {"description": "test"}

        response = client.post("/team", data=data, headers={"x-access-token": token})
        assert response.status_code == 400
        assert "missing data" in response.json["message"]

    @staticmethod
    def test_add_team_missing_description(client, token):
        data = {"name": "test"}

        response = client.post("/team", data=data, headers={"x-access-token": token})
        assert response.status_code == 400
        assert "missing data" in response.json["message"]

    @staticmethod
    def test_remove_invalid_team(client, token):
        response = client.delete("/team/9999999", headers={"x-access-token": token})
        assert response.status_code == 404
        assert "team not found" in response.json["message"]

    @staticmethod
    def test_update_invalid_team(client, token):
        data = {"name": "test234"}

        response = client.put("/team/999999", data=data, headers={"x-access-token": token})
        assert response.status_code == 404
        assert "team not found" in response.json["message"]

