from django.contrib import admin
from .models import Task
# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display=('course','title','description','deadline','status')
admin.site.register(Task,TaskAdmin)