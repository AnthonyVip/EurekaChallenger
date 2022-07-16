import unittest
from app.v1.model.user_queries import UserQueries
from app.v1.service.auth_service import AuthService
from fastapi.testclient import TestClient
from main import app


"""
module for unit tests
"""


class TestUserQuery(unittest.TestCase):
    """
    ## Unit test for UserQueries class
    actual test:
    - check_email
    - update_login
    """
    @classmethod
    def setUpClass(cls):
        cls.QueryClass = UserQueries()
        cls.email_true = "anthony@eurekalabs.io"
        cls.email_false = "other@email.com"
        cls.userid_true = 1
        cls.userid_false = 99999

    def test_check_email(self):
        self.assertTrue(self.QueryClass.check_email(self.email_true))
        self.assertFalse(self.QueryClass.check_email(self.email_false))

    def test_update_login(self):
        _old_login = self.QueryClass.get_last_login(self.userid_true)
        self.QueryClass.update_login(self.userid_true)
        _new_login = self.QueryClass.get_last_login(self.userid_true)
        self.assertNotEqual(_old_login, _new_login)
        self.assertFalse(self.QueryClass.get_last_login(self.userid_false))
        self.assertFalse(self.QueryClass.update_login(self.userid_false))


class TestAuthService(unittest.TestCase):
    """
    ## Unit test for AuthService class
    actual test:
    - authenticate_user
    """
    @classmethod
    def setUpClass(cls):
        cls.AuthClass = AuthService()
        cls.email_true = "anthony@eurekalabs.io"
        cls.email_false = "other@email.com"
        cls.password_true = "test1234"
        cls.password_false = "test1235"

    def test_authenticate_user(self):
        self.assertTrue(self.AuthClass.authenticate_user(self.email_true, self.password_true))  # noqa: E501
        self.assertFalse(self.AuthClass.authenticate_user(self.email_false, self.password_false))  # noqa: E501
        self.assertFalse(self.AuthClass.authenticate_user(self.email_true, self.password_false))  # noqa: E501


class TestEndpoints(unittest.TestCase):
    """
    ## Unit test for Endpoints class
    actual test:
    - login_for_access_token
    """
    @classmethod
    def setUpClass(cls):
        cls.client = TestClient(app)
        cls.email_true = "anthony@eurekalabs.io"
        cls.email_false = "other@email.com"
        cls.password_true = "test1234"
        cls.password_false = "test1235"

    def test_login_for_access_token(self):
        response = self.client.post("/api/v1/user/login/", json={"email": self.email_true, "password": self.password_true})  # noqa: E501
        self.assertEqual(response.status_code, 200)
        bad_response = self.client.post("/api/v1/user/login/", json={"email": self.email_false, "password": self.password_false})  # noqa: E501
        self.assertEqual(bad_response.status_code, 401)


if __name__ == '__main__':
    unittest.main()
