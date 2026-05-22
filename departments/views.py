from django.shortcuts import get_object_or_404, render

from .models import Department


def department_list(request):
    departments = Department.objects.all().order_by("code")
    return render(
        request,
        "departments/department_list.html",
        {"departments": departments},
    )


def department_detail(request, department_id):
    department = get_object_or_404(Department, id=department_id)
    courses = department.courses.all().order_by("course_code")
    return render(
        request,
        "departments/department_detail.html",
        {"department": department, "courses": courses},
    )
