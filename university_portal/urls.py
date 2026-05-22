from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("admin/", admin.site.urls),
    path("departments/", include("departments.urls")),
    path("courses/", include("courses.urls")),
]
