from django.test import Client

from tests_monet.tests.models import Answer, Exam, Question, Student
from tests_monet.users.models import User


class ModelTest:
    def setUp(self):
        self.test_student = Student.objects.create(
            email="prueba@prueba.com", names="Test", surnames="Chavez"
        )
        self.test_exam = Exam.objects.create(
            name="Examen Prueba", description="Solo prueba"
        )
        self.test_question = Question.objects.create(
            number=1, description="Solo prueba", exam=self.test_exam, active=True
        )
        self.test_answer = Answer.objects.create(
            description="Solo prueba",
            question=self.test_question,
            student=self.test_student,
            active=True,
        )
        self.client = Client()
        self.test_user = User.objects.create_superuser(
            username="superuser", password="secret", email="admin@example.com"
        )
        self.client.force_login(self.test_user)
