from rest_framework import viewsets
from tests_monet.tests.api.serializers import CreateAnswerSerializer, ListAnswerSerializer, RetrieveAnswerSerializer, UpdateAnswerSerializer
from tests_monet.tests.models import Answer
from tests_monet.tests.paginations import Pagination
from tests_monet.tests.permissions import IsStudent

from drf_spectacular.utils import extend_schema, extend_schema_view

@extend_schema_view(
    list = extend_schema(description="Permite obtener una lista de respuestas según estudiante"),
    retrieve = extend_schema(description="Permite obtener el detalle de respuesta según estudiante"),
    create = extend_schema(description="Permite crear una respuesta según estudiante"),
    partial_update = extend_schema(description="Permite actualizar una respuesta según estudiante"),
    delete = extend_schema(description="Permite eliminar una respuesta según estudiante"),
)
class AnswerViewSet(viewsets.ModelViewSet):
    permission_classes = (IsStudent,)
    pagination_class = Pagination

    def get_queryset(self):
        queryset = Answer.objects.filter(student__email=self.request.user.email)
        if self.action == "retrieve" or self.action == "list":
            queryset = queryset.filter(active=True)
        return queryset

    def get_serializer_class(self):
        serializer_class = ListAnswerSerializer
        if self.action == "retrieve":
            serializer_class = RetrieveAnswerSerializer
        if self.action == "partial_update":
            serializer_class = UpdateAnswerSerializer
        if self.action == "create":
            serializer_class = CreateAnswerSerializer
        return serializer_class