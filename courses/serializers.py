from rest_framework import serializers

from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    department_name = serializers.CharField(
        source="department.name",
        read_only=True,
    )

    class Meta:
        model = Course
        fields = [
            "id",
            "department",
            "department_name",
            "title",
            "course_code",
            "description",
            "credits",
            "level",
            "is_active",
        ]
