from django.contrib import admin
from .models import Discussion
# Register your models here.
class DiscussionAdmin(admin.ModelAdmin):
    list_display=('course','user','message','timestamp')
admin.site.register(Discussion,DiscussionAdmin)