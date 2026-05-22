from django.db import models

from courses.models import Course


class Student(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.CharField(max_length=255, unique=True)
    student_number = models.CharField(max_length=30, unique=True)
    major_course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="students",
    )
    enrollment_year = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student_number} - {self.full_name}"
