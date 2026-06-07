from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from .models import AuditLog, Enrollment
from .serializers import AuditLogSerializer, EnrollmentSerializer


class EnrollmentViewSet(ModelViewSet):
    queryset = Enrollment.objects.select_related("student", "course").order_by("id")
    serializer_class = EnrollmentSerializer
    permission_classes = [AllowAny]


class AuditLogViewSet(ReadOnlyModelViewSet):
    queryset = AuditLog.objects.all().order_by("-created_at")
    serializer_class = AuditLogSerializer
    permission_classes = [AllowAny]
