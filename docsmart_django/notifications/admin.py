from django.contrib import admin
from .models import Notification
from django.db import models
from mdeditor.widgets import MDEditorWidget


# Register your models here.
class NotificationsAdmin(admin.ModelAdmin):
    list_display = ['subject', 'user', 'created_at', 'updated_at']
    fields = ['subject', 'user', 'content']

    formfield_overrides = {
        models.TextField: {'widget': MDEditorWidget}
    }


admin.site.register(Notification, NotificationsAdmin)
