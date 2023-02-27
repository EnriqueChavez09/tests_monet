from django.test import TestCase

from tests_monet.tests.tests.model_test import ModelTest


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
        self.assertEqual(str(self.test_question), "Examen Prueba - N°01 - Solo prueba")

    def tearDown(self):
        self.test_question.delete()


class AnswerModelTest(ModelTest, TestCase):
    def test_str(self):
        self.assertEqual(str(self.test_answer), "Solo prueba")

    def tearDown(self):
        self.test_answer.delete()
