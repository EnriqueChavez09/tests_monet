from django.urls import reverse


def get_admin_view(obj: object) -> str:
    return reverse(
        f"admin:{obj._meta.app_label}_{type(obj).__name__.lower()}_change",
        args=(obj.pk,),
    )


def get_admin_changelist(obj: object) -> str:
    return reverse(
        "admin:{}_{}_changelist".format(
            obj._meta.app_label, type(obj).__name__.lower()
        ),
    )


def get_admin_add(obj: object) -> str:
    return reverse(
        f"admin:{obj._meta.app_label}_{type(obj).__name__.lower()}_add",
    )
