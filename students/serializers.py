from rest_framework import serializers

from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    major_course_title = serializers.CharField(
        source="major_course.title",
        read_only=True,
    )

    class Meta:
        model = Student
        fields = [
            "id",
            "full_name",
            "email",
            "student_number",
            "major_course",
            "major_course_title",
            "enrollment_year",
            "is_active",
            "created_at",
        ]
