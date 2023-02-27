from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "tests_monet.users"
    verbose_name = _("APP USUARIO")

    # def ready(self):
    #     try:
    #         import tests_monet.users.signals  # noqa F401
    #     except ImportError:
    #         pass
