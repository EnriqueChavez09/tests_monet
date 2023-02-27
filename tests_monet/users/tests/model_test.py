from django.test import Client

from tests_monet.users.models import User


class ModelTest:
    def setUp(self):
        self.client = Client()
        self.test_user = User.objects.create_superuser(
            username="superuser", password="secret", email="admin@example.com"
        )
        self.client.force_login(self.test_user)
