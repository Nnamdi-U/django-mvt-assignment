from django.db import transaction
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from .models import AuditLog, Enrollment
from .serializers import AuditLogSerializer, EnrollmentSerializer


class EnrollmentViewSet(ModelViewSet):
    queryset = Enrollment.objects.select_related("student", "course").order_by("id")
    serializer_class = EnrollmentSerializer
    permission_classes = [AllowAny]
    filterset_fields = ["student", "course", "status"]
    search_fields = [
        "student__full_name",
        "student__student_number",
        "course__course_code",
    ]
    ordering_fields = ["enrolled_at"]

    def perform_create(self, serializer):
        with transaction.atomic():
            serializer.save()


class AuditLogViewSet(ReadOnlyModelViewSet):
    queryset = AuditLog.objects.all().order_by("-created_at")
    serializer_class = AuditLogSerializer
    permission_classes = [AllowAny]
    filterset_fields = ["action", "model_name"]
    ordering_fields = ["created_at"]
