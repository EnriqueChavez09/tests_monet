from django.db import models
from model_utils.models import TimeStampedModel

from tests_monet.users.models import User


class Student(User):
    names = models.CharField("Nombres", max_length=100)
    surnames = models.CharField("Apellidos", max_length=100)
    active = models.BooleanField(
        "¿Activo?",
        default=True,
        help_text="No es necesario eliminar un estudiante, basta con desactivar para que ya no se muestre en la app",
    )

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"
        ordering = ["created"]


class Exam(TimeStampedModel):
    name = models.CharField("Nombre", max_length=100)
    description = models.TextField(
        "Descripción", help_text="Escriba un breve descripción del examen"
    )
    active = models.BooleanField(
        "¿Activo?",
        default=True,
        help_text="No es necesario eliminar un examen, basta con desactivar para que ya no se muestre en la app",
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Examen"
        verbose_name_plural = "Exámenes"
        ordering = ["created"]


class Question(TimeStampedModel):
    exam = models.ForeignKey(
        Exam,
        on_delete=models.CASCADE,
        related_name="questions",
        verbose_name="Examen",
    )
    number = models.PositiveIntegerField(
        "N°",
        help_text="Es el número de la pregunta, también sirve para ordenarlo de menor a mayor",
    )
    description = models.TextField(
        "Descripción", help_text="Escriba el enunciado de la pregunta"
    )
    active = models.BooleanField(
        "¿Activo?",
        default=True,
        help_text="No es necesario eliminar una pregunta, basta con desactivar para que ya no se muestre en la app",
    )

    def __str__(self):
        return f"{self.description}"

    class Meta:
        verbose_name = "Pregunta"
        verbose_name_plural = "Preguntas"
        ordering = ["number"]


class Answer(TimeStampedModel):
    question = models.OneToOneField(
        Question,
        on_delete=models.SET_NULL,
        null=True,
        related_name="answer",
        verbose_name="Pregunta",
    )
    student = models.OneToOneField(
        Student,
        on_delete=models.CASCADE,
        related_name="answer",
        verbose_name="Estudiante",
    )
    description = models.TextField(
        "Descripción", help_text="Escriba la respuesta de la pregunta"
    )
    active = models.BooleanField(
        "¿Activo?",
        default=True,
        help_text="No es necesario eliminar una respuesta, basta con desactivar para que ya no se muestre en la app",
    )

    def __str__(self):
        return f"{self.description}"

    class Meta:
        verbose_name = "Respuesta"
        verbose_name_plural = "Respuestas"
        ordering = ["created"]
