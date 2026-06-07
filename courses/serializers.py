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

    def validate_credits(self, value):
        if value <= 0:
            raise serializers.ValidationError("Credits must be greater than 0.")
        return value

    def validate_level(self, value):
        allowed_levels = [100, 200, 300, 400, 500]
        if value not in allowed_levels:
            raise serializers.ValidationError(
                "Level must be 100, 200, 300, 400, or 500."
            )
        return value
