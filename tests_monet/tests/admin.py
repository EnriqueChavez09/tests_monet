from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from tests_monet.tests.models import Answer, Exam, Question, Student
from tests_monet.users.admin import UserAdmin


@admin.register(Student)
class StudentAdmin(UserAdmin):
    fieldsets = (
        (
            _("Credenciales"),
            {
                "fields": (
                    "email",
                    "password",
                )
            },
        ),
        (
            _("Información Personal"),
            {
                "fields": (
                    "names",
                    "surnames",
                    "active",
                ),
            },
        ),
    )

    list_display = [
        "id",
        "email",
        "names",
        "surnames",
        "active",
    ]
    list_display_links = ["id", "email"]


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            _("Información General"),
            {
                "fields": (
                    "name",
                    "description",
                    "active",
                ),
            },
        ),
    )

    list_display = [
        "id",
        "name",
        "description",
        "active",
    ]
    list_display_links = ["id", "name"]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            _("Información General"),
            {
                "fields": (
                    "exam",
                    "number",
                    "description",
                    "active",
                ),
            },
        ),
    )

    list_display = [
        "id",
        "exam",
        "number",
        "description",
        "active",
    ]
    list_display_links = ["id", "exam"]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "question",
        "student",
        "description",
        "active",
    ]
    list_display_links = ["id", "question"]

    def get_fieldsets(self, request, obj):
        super().get_fieldsets(request, obj)
        try:
            Student.objects.get(email=request.user.email)
            fieldsets = (
                (
                    _("Información General"),
                    {
                        "fields": (
                            "question",
                            "description",
                            "active",
                        ),
                    },
                ),
            )
        except Exception:
            fieldsets = (
                (
                    _("Información General"),
                    {
                        "fields": (
                            "question",
                            "student",
                            "description",
                            "active",
                        ),
                    },
                ),
            )
        return fieldsets

    def get_queryset(self, request):
        qs = self.model._default_manager.get_queryset()
        try:
            student = Student.objects.get(email=request.user.email)
            qs = qs.filter(student=student)
        except Exception:
            pass
        return qs

    def save_model(self, request, obj, form, change):
        if not change:
            try:
                student = Student.objects.get(email=request.user.email)
                form.instance.student = student
                form.instance.save()
            except Exception:
                pass
        obj.save()
