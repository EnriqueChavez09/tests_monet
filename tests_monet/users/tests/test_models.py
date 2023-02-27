from django.test import TestCase

from tests_monet.users.models import User


class ModelTest:
    def setUp(self):
        self.test_user = User(email="admin@prueba.com")
        self.test_user.save()


class UserModelTest(ModelTest, TestCase):
    def test_str(self):
        self.assertEqual(str(self.test_user), "admin@prueba.com")

    def tearDown(self):
        self.test_user.delete()
