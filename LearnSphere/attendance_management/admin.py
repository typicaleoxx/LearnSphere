from django.contrib import admin
from .models import Attendance
# Register your models here.
class AttendanceAdmin(admin.ModelAdmin):
    list_display=('user','course','date','status')
admin.site.register(Attendance,AttendanceAdmin)