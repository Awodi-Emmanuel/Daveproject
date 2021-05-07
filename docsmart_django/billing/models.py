from datetime import datetime

from django.db import models

# Create your models here.
from company.models import Company
from payments.models import Payment


class BillingPlans(models.Model):
    plan_id = models.SlugField(blank=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, null=True, blank=True)
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

    class Meta:
        db_table = 'plan'
        ordering = ['-created_at']

    def __str__(self):
        return '{} - {}'.format(self.name, self.created_at)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.plan_id = slugify(self.name)
        super(BillingPlans, self).save(*args, **kwargs)


class Subscription(models.Model):
    user = models.ForeignKey(Company, on_delete=models.DO_NOTHING, db_column='company', null=True, blank=True)
    plan = models.ForeignKey(BillingPlans, on_delete=models.DO_NOTHING, db_column='plan', null=True, blank=True)
    payment = models.OneToOneField(Payment, on_delete=models.DO_NOTHING, db_column='payment', null=True, blank=True)
    billing_period = models.IntegerField()
    periods = (
        ('day', 'Day'),
        ('week', 'Week'),
        ('month', 'Month'),
        ('year', 'Year'),
    )
    billing_period_unit = models.CharField(max_length=10, choices=periods)
    plan_amount = models.FloatField()
    plan_quantity = models.IntegerField()
    plan_unit_price = models.FloatField()
    subscription_id = models.CharField(max_length=100)
    next_billing_at = models.DateTimeField()
    created_at = models.DateTimeField()
    activated_at = models.DateTimeField()
    status = models.BooleanField()
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        db_table = 'subscription'
        ordering = ['-created_at']

    def __str__(self):
        return '{} - {}'.format(self.subscription_id, self.created_at)

    def get_days_left(self):
        return (self.next_billing_at - datetime.now()).days

