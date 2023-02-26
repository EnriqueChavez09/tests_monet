from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver

from tests_monet.tests.models import Student


@receiver(post_save, sender=Student)
def assign_staff(sender, instance, created, **kwargs):
    if created:
        groups = Group.objects.filter(name="Estudiante").values_list("id", flat=True)
        instance.is_staff = True
        instance.groups.set(groups)
        instance.save()
