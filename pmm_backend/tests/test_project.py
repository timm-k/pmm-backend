import json


class TestProject:
    @staticmethod
    def test_add_and_list_project(client, token):
        data = {"name": "test_name",
                "description": "test_description",
                "start_timestamp": 19299,
                "end_timestamp": 229999}

        response = client.post("/project", data=data, headers={"x-access-token": token})
        project_id = response.json["project_id"]
        assert response.status_code == 200
        assert response.json["message"] == "success"

        response = client.get("/project/list", headers={"x-access-token": token})
        assert response.status_code == 200

        user_list = json.loads(response.data)
        for u in user_list:
            if int(project_id) == int(u['project_id']):
                assert u['name'] == "test_name"
                assert u['description'] == "test_description"
                assert u['start_timestamp'] == 19299
                assert u['end_timestamp'] == 229999

        return project_id

    @staticmethod
    def test_edit_and_list_project(client, token, project_id):
        data = {"name": "test_name_edit",
                "description": "test_description_edit",
                "start_timestamp": 99,
                "end_timestamp": 2292999}

        response = client.put("/project/" + str(project_id), data=data, headers={"x-access-token": token})
        assert response.status_code == 200

        response = client.get("/project/list", headers={"x-access-token": token})
        assert response.status_code == 200

        project_list = json.loads(response.data)
        for t in project_list:
            if int(project_id) == int(t['project_id']):
                assert t['name'] == "test_name_edit"
                assert t['description'] == "test_description_edit"
                assert t['start_timestamp'] == 99
                assert t['end_timestamp'] == 2292999

    @staticmethod
    def test_remove_project(client, token, project_id):
        response = client.delete("/project/" + str(project_id), headers={"x-access-token": token})
        assert response.status_code == 200

    @staticmethod
    def test_add_project_missing_name(client, token):
        data = {"description": "test_description_edit",
                "start_timestamp": 99,
                "end_timestamp": 2292999}

        response = client.post("/project", data=data, headers={"x-access-token": token})
        assert response.status_code == 400

    @staticmethod
    def test_add_project_missing_description(client, token):
        data = {"name": "test",
                "start_timestamp": 99,
                "end_timestamp": 2292999}

        response = client.post("/project", data=data, headers={"x-access-token": token})
        assert response.status_code == 400

    @staticmethod
    def test_add_project_missing_timestamps(client, token):
        data = {"name": "test",
                "description": "test",
                "end_timestamp": 2292999}

        response = client.post("/project", data=data, headers={"x-access-token": token})
        assert response.status_code == 400

        data = {"name": "test",
                "description": "test",
                "start_timestamp": 2292999}

        response = client.post("/project", data=data, headers={"x-access-token": token})
        assert response.status_code == 400


    @staticmethod
    def test_remove_invalid_project(client, token):
        response = client.delete("/project/9999999", headers={"x-access-token": token})
        assert response.status_code == 404

    @staticmethod
    def test_update_invalid_project(client, token):
        data = {"name": "test234"}

        response = client.put("/project/999999", data=data, headers={"x-access-token": token})
        assert response.status_code == 404

