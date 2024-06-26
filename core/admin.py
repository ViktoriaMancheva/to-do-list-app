from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_filter = ["pub_date"]
    search_fields = ["title"]


admin.site.register(Task, TaskAdmin)

