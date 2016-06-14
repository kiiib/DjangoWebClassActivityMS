from django.contrib import admin
from app.models import Activity, User, JOINT_ACTIVITY

class ActivityAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'address', 'price', 'deadline')
    search_fields = ('title', 'date')
    ordering = ('deadline',)

class UserAdmin(admin.ModelAdmin):
    list_display = ('id_number', 'name', 'sex', 'tel')
    search_fields = ('id_number', 'name')
    ordering = ('id_number',)

class JOINT_ACTIVITYAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'act_id')
    search_fields = ('user_id', 'act_id')
    ordering = ('act_id',)

admin.site.register(Activity, ActivityAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(JOINT_ACTIVITY, JOINT_ACTIVITYAdmin)