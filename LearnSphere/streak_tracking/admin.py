from django.contrib import admin
from .models import Streak
# Register your models here.
class StreakAdmin(admin.ModelAdmin):
    list_display=('user','last_active_date','streak_count')
admin.site.register(Streak,StreakAdmin)