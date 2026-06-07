from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from .models import Student
from .serializers import StudentSerializer


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.select_related("major_course").order_by("id")
    serializer_class = StudentSerializer
    permission_classes = [AllowAny]
