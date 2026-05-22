from django.shortcuts import get_object_or_404, render

from .models import Course


def course_list(request):
    courses = Course.objects.select_related("department").all().order_by("course_code")
    return render(request, "courses/course_list.html", {"courses": courses})


def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, "courses/course_detail.html", {"course": course})
