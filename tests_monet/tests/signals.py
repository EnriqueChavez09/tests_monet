from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission, Group
from tests_monet.tests.models import Answer
from tests_monet.tests.models import Student


@receiver(post_save, sender=Student)
def assign_staff(sender, instance, created, **kwargs):
    if created:
        groups = Group.objects.filter(name="Estudiante").values_list("id", flat=True)
        instance.is_staff = True
        instance.groups.set(groups)
        instance.save()

@receiver(post_save, sender=Student)
def assign_group(sender, instance, created, **kwargs):
    if created:
        content_type = ContentType.objects.get_for_model(Answer)
        permissions = Permission.objects.filter(content_type=content_type).values_list("id",flat=True)
        group,_ = Group.objects.get_or_create(name="Estudiante")
        group.permissions.set(permissions)
        instance.groups.set([group.pk])
        instance.save()