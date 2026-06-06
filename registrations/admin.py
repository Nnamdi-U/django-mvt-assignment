from django.contrib import admin

from .models import AuditLog, Enrollment


admin.site.register(Enrollment)
admin.site.register(AuditLog)
