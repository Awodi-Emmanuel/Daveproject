from django.contrib import admin
from .models import FAQ
from django.db import models
from mdeditor.widgets import MDEditorWidget


# Register your models here.
class FAQAdmin(admin.ModelAdmin):
    list_display = ['subject', 'category', 'created_at', 'updated_at']
    fields = ['subject', 'category', 'content']

    formfield_overrides = {
        models.TextField: {'widget': MDEditorWidget}
    }


admin.site.register(FAQ, FAQAdmin)
