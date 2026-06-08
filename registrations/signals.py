from django.db.models.signals import post_save
from django.dispatch import receiver

from courses.models import Course
from students.models import Student

from .models import AuditLog, Enrollment


@receiver(post_save, sender=Student)
def log_student_created(sender, instance, created, **kwargs):
    if created:
        AuditLog.objects.create(
            action="student_created",
            model_name="Student",
            object_id=instance.id,
            message=(
                f"Student {instance.student_number} - "
                f"{instance.full_name} was created."
            ),
        )


@receiver(post_save, sender=Course)
def log_course_created(sender, instance, created, **kwargs):
    if created:
        AuditLog.objects.create(
            action="course_created",
            model_name="Course",
            object_id=instance.id,
            message=f"Course {instance.course_code} - {instance.title} was created.",
        )


@receiver(post_save, sender=Enrollment)
def log_enrollment_created(sender, instance, created, **kwargs):
    if created:
        AuditLog.objects.create(
            action="enrollment_created",
            model_name="Enrollment",
            object_id=instance.id,
            message=(
                f"Student {instance.student.student_number} enrolled in "
                f"{instance.course.course_code}."
            ),
        )
