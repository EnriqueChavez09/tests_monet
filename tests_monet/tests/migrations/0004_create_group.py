from django.db import migrations
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from tests_monet.tests.models import Answer

def forwards_func(apps, schema_editor):
    content_type = ContentType.objects.get_for_model(Answer)
    permissions = Permission.objects.filter(content_type=content_type).values_list("id",flat=True)
    Group = apps.get_model("auth", "Group")
    group = Group(name="Estudiante")
    group.save()
    group.permissions.set(permissions)

def reverse_func(apps, schema_editor):
    Group = apps.get_model("auth", "Group")
    db_alias = schema_editor.connection.alias
    Group.objects.using(db_alias).all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0003_rename_test_exam_rename_test_question_exam'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]