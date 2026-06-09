from rest_framework import serializers

from courses.serializers import CourseSerializer

from .models import Department


class DepartmentSerializer(serializers.ModelSerializer):
    course_count = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = [
            "id",
            "name",
            "code",
            "description",
            "building_name",
            "created_at",
            "course_count",
        ]

    def get_course_count(self, department):
        return department.courses.count()


class DepartmentDetailSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = Department
        fields = [
            "id",
            "name",
            "code",
            "description",
            "building_name",
            "created_at",
            "courses",
        ]
