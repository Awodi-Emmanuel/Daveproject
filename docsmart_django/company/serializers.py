from rest_framework import serializers
from company.models import Company



class CompanySerializer(serializers.ModelSerializer):
    
    company_email = serializers.EmailField(max_length=255, min_length=4)
    company_name = serializers.CharField(max_length=255, min_length=2)

    class Meta:
        model = Company
        fields = ['company_email', 'company_name',]

    def validate(self, attrs):
        company_email = attrs.get('company_email', '')
        company_name = attrs.get('company_name', '')
        
        if company_email is None:
            raise serializers.ValidationError(
                {'company_email': ('Company Email cannot be empty')})
        if company_name is None:
            raise serializers.ValidationError(
                {'company_name': ('Company Name cannot be empty')})
        if Company.objects.filter(company_email=company_email).exists():
            raise serializers.ValidationError(
                {'company_email': ('Company email is already in use')})
        if Company.objects.filter(company_name=company_name.lower()).exists():
            raise serializers.ValidationError(
                {'company_name': ('Company email is already in use')})
        return super().validate(attrs)
    
    def create(self, validated_data):
        return Company.objects.create_company(**validated_data)


    