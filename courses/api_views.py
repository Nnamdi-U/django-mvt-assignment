from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from .models import Course
from .serializers import CourseSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.select_related("department").order_by("id")
    serializer_class = CourseSerializer
    permission_classes = [AllowAny]
    filterset_fields = ["department", "is_active"]
    search_fields = ["title", "course_code", "description"]
    ordering_fields = ["course_code", "title", "credits", "level"]
