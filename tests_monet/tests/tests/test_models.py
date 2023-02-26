from django.test import TestCase

from tests_monet.tests.models import Answer, Question, Student, Exam


class ModelTest:
    def setUp(self):
        self.test_student = Student(
            email="prueba@prueba.com", names="Test", surnames="Chavez"
        )
        self.test_student.save()
        self.test_exam = Exam(name="Examen Prueba", description="Solo prueba")
        self.test_exam.save()
        self.test_question = Question(
            number=1, description="Solo prueba", exam=self.test_exam, active=True
        )
        self.test_question.save()
        self.test_answer = Answer(
            description="Solo prueba",
            question=self.test_question,
            student=self.test_student,
            active=True,
        )
        self.test_answer.save()


class StudentModelTest(ModelTest, TestCase):
    def test_str(self):
        self.assertEqual(str(self.test_student), "prueba@prueba.com")

    def tearDown(self):
        self.test_student.delete()


class TestModelTest(ModelTest, TestCase):
    def test_str(self):
        self.assertEqual(str(self.test_exam), "Examen Prueba")

    def tearDown(self):
        self.test_exam.delete()


class QuestionModelTest(ModelTest, TestCase):
    def test_str(self):
        self.assertEqual(str(self.test_question), "Solo prueba")

    def tearDown(self):
        self.test_question.delete()


class AnswerModelTest(ModelTest, TestCase):
    def test_str(self):
        self.assertEqual(str(self.test_answer), "Solo prueba")

    def tearDown(self):
        self.test_answer.delete()
