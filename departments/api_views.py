from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from .models import Department
from .serializers import DepartmentDetailSerializer, DepartmentSerializer


class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all().order_by("id")
    serializer_class = DepartmentSerializer
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return DepartmentDetailSerializer
        return DepartmentSerializer
