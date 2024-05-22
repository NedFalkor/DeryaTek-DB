from django.contrib import admin

from dt_users.models.custom_user import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'date_joined', 'is_staff')
    search_fields = ('email', 'username')
    list_filter = ('is_staff', 'is_superuser')
    ordering = ('-date_joined',)
