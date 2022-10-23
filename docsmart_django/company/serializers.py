from rest_framework import serializers
from company.models import Company


class CompanySerializer(serializers.ModelSerializer):
    company_number = serializers.CharField(max_length=255, min_length=4)
    company_name = serializers.CharField(max_length=255, min_length=2)
    company_size = serializers.IntegerField()

    class Meta:
        model = Company
        fields = ['company_name', 'company_number', 'company_size']

    def validate(self, attrs):
        company_number = attrs.get('company_number', '')
        company_name = attrs.get('company_name', '')
        company_size = attrs.get('company_size', '')

        if company_number is None:
            raise serializers.ValidationError(
                {'company_number': 'Company number cannot be empty'})
        if company_name is None:
            raise serializers.ValidationError(
                {'company_name': 'Company Name cannot be empty'})
        if company_size < 5:
            raise serializers.ValidationError(
                {'company_size': 'Company size must be be 5 or above'})
        if Company.objects.filter(company_email=company_number).exists():
            raise serializers.ValidationError(
                {'company_number': 'Company number is already in use'})
        if Company.objects.filter(company_name=company_name.lower()).exists():
            raise serializers.ValidationError(
                {'company_name': 'Company name is already in use'})
        return super().validate(attrs)

    def create(self, validated_data):
        return Company.objects.create_company(**validated_data)


class CompanyUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company

        fields = '__all__'
