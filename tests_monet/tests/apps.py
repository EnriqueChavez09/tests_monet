from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TestsConfig(AppConfig):
    name = "tests_monet.tests"
    verbose_name = _("APP TEST")