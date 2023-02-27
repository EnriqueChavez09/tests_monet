from django.test import TestCase

from tests_monet.users.tests.model_test import ModelTest


class UserModelTest(ModelTest, TestCase):
    def test_str(self):
        self.assertEqual(str(self.test_user), "admin@example.com")

    def tearDown(self):
        self.test_user.delete()
