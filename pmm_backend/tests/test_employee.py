import json


class TestEmployee:
    @staticmethod
    def test_add_and_list_employee(client, token):
        data = {"first_name": "test_employee_first",
                "last_name": "test_employee_last"}

        response = client.post("/employee", data=data, headers={"x-access-token": token})
        employee_id = response.json["employee_id"]
        assert response.status_code == 200
        assert response.json["message"] == "success"

        response = client.get("/employee/list", headers={"x-access-token": token})
        assert response.status_code == 200

        user_list = json.loads(response.data)
        for u in user_list:
            if int(employee_id) == int(u['employee_id']):
                assert u['first_name'] == "test_employee_first"
                assert u['last_name'] == "test_employee_last"

        return employee_id

    @staticmethod
    def test_edit_and_list_employee(client, token, employee_id):
        data = {"first_name": "test_employee_first_edit",
                "last_name": "test_employee_last_edit"}

        response = client.put("/employee/" + str(employee_id), data=data, headers={"x-access-token": token})
        assert response.status_code == 200
        assert response.json["message"] == "success"

        response = client.get("/employee/list", headers={"x-access-token": token})
        assert response.status_code == 200

        employee_list = json.loads(response.data)
        for t in employee_list:
            if int(employee_id) == int(t['employee_id']):
                assert t['first_name'] == "test_employee_first_edit"
                assert t['last_name'] == "test_employee_last_edit"

    @staticmethod
    def test_remove_employee(client, token, employee_id):
        response = client.delete("/employee/" + str(employee_id), headers={"x-access-token": token})
        assert response.status_code == 200
        assert response.json["message"] == "success"

    @staticmethod
    def test_add_employee_missing_first_name(client, token):
        data = {"last_name": "test"}

        response = client.post("/employee", data=data, headers={"x-access-token": token})
        assert response.status_code == 400

    @staticmethod
    def test_add_employee_missing_last_name(client, token):
        data = {"first_name": "test"}

        response = client.post("/employee", data=data, headers={"x-access-token": token})
        assert response.status_code == 400


    @staticmethod
    def test_remove_invalid_employee(client, token):
        response = client.delete("/employee/9999999", headers={"x-access-token": token})
        assert response.status_code == 404

    @staticmethod
    def test_update_invalid_employee(client, token):
        data = {"name": "test234"}

        response = client.put("/employee/999999", data=data, headers={"x-access-token": token})
        assert response.status_code == 404

