from django.test import TestCase

from tests_monet.tests.tests.model_test import ModelTest
from tests_monet.utils.helpers import (
    get_admin_add,
    get_admin_changelist,
    get_admin_view,
)


class TestStudentAdmin(ModelTest, TestCase):
    def test_view_student(self):
        response = self.client.get(get_admin_view(self.test_student))
        self.assertEqual(response.status_code, 200)

    def test_changelist_students(self):
        response = self.client.get(get_admin_changelist(self.test_student))
        self.assertEqual(response.status_code, 200)

    def test_add_student(self):
        response = self.client.get(get_admin_add(self.test_student))
        self.assertEqual(response.status_code, 200)


class TestExamAdmin(ModelTest, TestCase):
    def test_view_exam(self):
        response = self.client.get(get_admin_view(self.test_exam))
        self.assertEqual(response.status_code, 200)

    def test_changelist_exams(self):
        response = self.client.get(get_admin_changelist(self.test_exam))
        self.assertEqual(response.status_code, 200)

    def test_add_exam(self):
        response = self.client.get(get_admin_add(self.test_exam))
        self.assertEqual(response.status_code, 200)


class TestQuestionAdmin(ModelTest, TestCase):
    def test_view_question(self):
        response = self.client.get(get_admin_view(self.test_question))
        self.assertEqual(response.status_code, 200)

    def test_changelist_questions(self):
        response = self.client.get(get_admin_changelist(self.test_question))
        self.assertEqual(response.status_code, 200)

    def test_add_question(self):
        response = self.client.get(get_admin_add(self.test_question))
        self.assertEqual(response.status_code, 200)


class TestAnswerAdmin(ModelTest, TestCase):
    def test_view_answer(self):
        response = self.client.get(get_admin_view(self.test_answer))
        self.assertEqual(response.status_code, 200)

    def test_changelist_answers(self):
        response = self.client.get(get_admin_changelist(self.test_answer))
        self.assertEqual(response.status_code, 200)

    def test_add_answer(self):
        response = self.client.get(get_admin_add(self.test_answer))
        self.assertEqual(response.status_code, 200)
