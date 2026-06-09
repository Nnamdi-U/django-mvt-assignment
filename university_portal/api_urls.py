from rest_framework.routers import DefaultRouter

from courses.api_views import CourseViewSet
from departments.api_views import DepartmentViewSet
from registrations.api_views import AuditLogViewSet, EnrollmentViewSet
from students.api_views import StudentViewSet

router = DefaultRouter()
router.register("departments", DepartmentViewSet, basename="api-department")
router.register("courses", CourseViewSet, basename="api-course")
router.register("students", StudentViewSet, basename="api-student")
router.register("enrollments", EnrollmentViewSet, basename="api-enrollment")
router.register("audit-logs", AuditLogViewSet, basename="api-audit-log")

urlpatterns = router.urls
