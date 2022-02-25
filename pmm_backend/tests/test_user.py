class TestUser:
    @staticmethod
    def test_login(client):
        response = client.post("/user/login",  data={"email": "test@test.com", "password": "ABC"})
        assert response.status_code == 201