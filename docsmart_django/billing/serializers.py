from rest_framework import serializers
from .models import BillingPlans


class FetchPlansSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingPlans
        fields = '__all__'
