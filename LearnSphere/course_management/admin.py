from django.contrib import admin
from .models import Course, Enrollment
# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "instructor",'description','duration')
admin.site.register(Course,CourseAdmin)

class EnrollmentAdmin(admin.ModelAdmin):
    list_display=('user','course','date_enrolled')
admin.site.register(Enrollment,EnrollmentAdmin)
