import json


class TestWorkPackage:
    @staticmethod
    def test_add_and_list_work_package(client, token, project_id):
        data = {"name": "test_name",
                "project_id": project_id,
                "description": "test_description",
                "start_timestamp": 19299,
                "end_timestamp": 229999}

        response = client.post("/package", data=data, headers={"x-access-token": token})
        work_package_id = response.json["work_package_id"]
        assert response.status_code == 200
        assert response.json["message"] == "success"

        response = client.get("/package/list", headers={"x-access-token": token})
        assert response.status_code == 200

        user_list = json.loads(response.data)
        for u in user_list:
            if int(work_package_id) == int(u['work_package_id']):
                assert u['name'] == "test_name"
                assert u['project_id'] == project_id
                assert u['description'] == "test_description"
                assert u['start_timestamp'] == 19299
                assert u['end_timestamp'] == 229999

        return work_package_id

    @staticmethod
    def test_edit_and_list_work_package(client, token, work_package_id, project_id):
        data = {"name": "test_name_edit",
                "description": "test_description_edit",
                "project_id": project_id,
                "start_timestamp": 11,
                "end_timestamp": 99999}

        response = client.put("/package/" + str(work_package_id), data=data, headers={"x-access-token": token})
        assert response.status_code == 200

        response = client.get("/package/list", headers={"x-access-token": token})
        assert response.status_code == 200

        work_package_list = json.loads(response.data)
        for t in work_package_list:
            if int(work_package_id) == int(t['work_package_id']):
                assert t['name'] == "test_name_edit"
                assert t['description'] == "test_description_edit"
                assert t['start_timestamp'] == 11
                assert t['end_timestamp'] == 99999

    @staticmethod
    def test_remove_work_package(client, token, work_package_id):
        response = client.delete("/package/" + str(work_package_id), headers={"x-access-token": token})
        assert response.status_code == 200

    @staticmethod
    def test_add_work_package_missing_name(client, token, project_id):
        data = {"description": "test_description_edit",
                "project_id": project_id,
                "start_timestamp": 99,
                "end_timestamp": 2292999}

        response = client.post("/package", data=data, headers={"x-access-token": token})
        assert response.status_code == 400

    @staticmethod
    def test_add_work_package_missing_description(client, token, project_id):
        data = {"name": "test",
                "project_id": project_id,
                "start_timestamp": 99,
                "end_timestamp": 2292999}

        response = client.post("/package", data=data, headers={"x-access-token": token})
        assert response.status_code == 400

    @staticmethod
    def test_add_work_package_missing_project_id(client, token):
        data = {"name": "test",
                "description": "test",
                "start_timestamp": 99,
                "end_timestamp": 2292999}

        response = client.post("/package", data=data, headers={"x-access-token": token})
        assert response.status_code == 400

    @staticmethod
    def test_add_work_package_missing_timestamps(client, token, project_id):
        data = {"description": "test_description",
                "name": "testname",
                "project_id": project_id,
                "start_timestamp": 99}

        response = client.post("/package", data=data, headers={"x-access-token": token})
        assert response.status_code == 400

        data = {"description": "test_description",
                "name": "testname",
                "project_id": project_id,
                "end_timestamp": 99}

        response = client.post("/package", data=data, headers={"x-access-token": token})
        assert response.status_code == 400

    @staticmethod
    def test_remove_invalid_work_package(client, token):
        response = client.delete("/package/9999999", headers={"x-access-token": token})
        assert response.status_code == 404

    @staticmethod
    def test_update_invalid_work_package(client, token):
        data = {"name": "test234"}

        response = client.put("/package/999999", data=data, headers={"x-access-token": token})
        assert response.status_code == 404

    @staticmethod
    def test_add_work_package_invlalid_project_id(client, token):
        data = {"name": "test",
                "description": "test",
                "project_id": 999999,
                "start_timestamp": 99,
                "end_timestamp": 2292999}

        response = client.post("/package", data=data, headers={"x-access-token": token})
        assert response.status_code == 400
