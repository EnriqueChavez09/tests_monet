from django.test import TestCase

from tests_monet.users.tests.model_test import ModelTest
from tests_monet.utils.helpers import (
    get_admin_add,
    get_admin_changelist,
    get_admin_view,
)


class TestUserAdmin(ModelTest, TestCase):
    def test_view_user(self):
        response = self.client.get(get_admin_view(self.test_user))
        self.assertEqual(response.status_code, 200)

    def test_changelist_users(self):
        response = self.client.get(get_admin_changelist(self.test_user))
        self.assertEqual(response.status_code, 200)

    def test_add_user(self):
        response = self.client.get(get_admin_add(self.test_user))
        self.assertEqual(response.status_code, 200)
