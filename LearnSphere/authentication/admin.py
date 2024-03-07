from django.contrib import admin
from .models import User
# Register your models here.
class AuthenticationAdmin(admin.ModelAdmin):
    list_display=('username','email','password')
admin.site.register(User,AuthenticationAdmin)