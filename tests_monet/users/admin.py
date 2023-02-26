from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

from tests_monet.users.forms import CustomUserChangeForm, CustomUserCreationForm

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    fieldsets = (
        (
            _("Información Personal"),
            {
                "fields": (
                    "email",
                    "password",
                )
            },
        ),
        (
            _("Permisos"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Fechas Importantes"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ["id", "email"]
    list_display_links = ["email"]
    search_fields = ["email"]
    list_filter = []


admin.site.unregister(Group)
