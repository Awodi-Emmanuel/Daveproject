from rest_framework import serializers
from .models import FAQ


class FetchSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['subject', 'category', 'content', 'created_at', 'updated_at']
