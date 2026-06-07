from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from .models import Student
from .serializers import StudentSerializer


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.select_related("major_course").order_by("id")
    serializer_class = StudentSerializer
    permission_classes = [AllowAny]
    filterset_fields = ["is_active", "enrollment_year"]
    search_fields = ["full_name", "email", "student_number"]
    ordering_fields = ["full_name", "enrollment_year", "created_at"]
