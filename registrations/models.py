from django.db import models

from courses.models import Course
from students.models import Student


class Enrollment(models.Model):
    ACTIVE = "active"
    COMPLETED = "completed"
    DROPPED = "dropped"

    STATUS_CHOICES = [
        (ACTIVE, "Active"),
        (COMPLETED, "Completed"),
        (DROPPED, "Dropped"),
    ]

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="enrollments",
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="enrollments",
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=ACTIVE,
    )
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["student", "course"],
                name="unique_student_course_enrollment",
            )
        ]

    def __str__(self):
        return f"{self.student.full_name} - {self.course.course_code}"
