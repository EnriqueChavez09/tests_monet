from rest_framework.permissions import BasePermission
from tests_monet.tests.models import Student

class IsStudent(BasePermission):
    def has_permission(self, request, view):
        try:
            Student.objects.get(email=request.user.email)
            return True
        except Exception:
            return False
