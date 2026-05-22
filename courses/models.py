from django.db import models

from departments.models import Department


class Course(models.Model):
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="courses",
    )
    title = models.CharField(max_length=200)
    course_code = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    credits = models.PositiveIntegerField()
    level = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.course_code} - {self.title}"
