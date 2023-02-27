from tests_monet.tests.models import Answer, Student
from rest_framework import serializers
from django.core.exceptions import ValidationError

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = [
            "id",
            "question",
            "description",
        ]

class RetrieveAnswerSerializer(serializers.ModelSerializer):
    class Meta(AnswerSerializer.Meta):
        fields = [
            "id",
            "question",
            "student",
            "description",
        ]

class ListAnswerSerializer(serializers.ModelSerializer):
    class Meta(AnswerSerializer.Meta):
        pass

class UpdateAnswerSerializer(serializers.ModelSerializer):
    class Meta(AnswerSerializer.Meta):
        pass

    def update(self, instance: Answer, validated_data: dict):
        instance.question = validated_data.get("name", instance.question)
        instance.description = validated_data.get("description", instance.description)
        instance.save()
        return instance
    
class CreateAnswerSerializer(serializers.ModelSerializer):
    class Meta(AnswerSerializer.Meta):
        pass

    def create(self, validated_data: dict):
        user = self.context["request"].user
        student = Student.objects.get(email=user.email)
        return Answer.objects.create(
            question=validated_data["question"],
            student=student,
            description=validated_data["description"],
        )
    
    def validate_question(self, value):
        user = self.context["request"].user
        student = Student.objects.get(email=user.email)
        try:
            answer = Answer.objects.get( question=value, student=student )
        except Exception:
            return value
        if answer:
            raise ValidationError(
                "Ya existe una respuesta a esta pregunta",
            )