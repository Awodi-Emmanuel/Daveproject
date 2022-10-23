from django.contrib import admin
from .models import User


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'date_joined', 'is_active', 'is_admin']
    fields = ['first_name', 'last_name', 'is_active', 'is_admin']


admin.site.register(User, UserAdmin)
