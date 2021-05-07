from django.contrib import admin
from .models import BillingPlans
from django.db import models
from mdeditor.widgets import MDEditorWidget

"""
    plan_id = models.SlugField(blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    period = models.IntegerField(default=1)
    periods = (
        ('day', 'Day'),
        ('week', 'Week'),
        ('month', 'Month'),
        ('year', 'Year'),
    )
    period_unit = models.CharField(max_length=10, choices=periods, default='month')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
"""


# Register your models here.
class PlansAdmin(admin.ModelAdmin):
    list_display = ['plan_id', 'name', 'price', 'period_unit']
    fields = ['name', 'description', 'price', 'period', 'period_unit']

    formfield_overrides = {
        models.TextField: {'widget': MDEditorWidget}
    }


admin.site.register(BillingPlans, PlansAdmin)
