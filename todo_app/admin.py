from django.contrib import admin
from .models import Task
# Register your models here.

# Overrid the addmin functionality
class TaskAdmin(admin.ModelAdmin):
    list_display =("task","isCompleted","updated_at")
    search_fields=("task",)

admin.site.register(Task,TaskAdmin)

