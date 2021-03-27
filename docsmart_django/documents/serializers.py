from django.contrib.auth import get_user_model
from permissions.models import DocumentPermission
from rest_framework import serializers
from .models import Document


class DocumentSerializer(serializers.ModelSerializer):

    name = serializers.CharField(
        max_length=255, min_length=8)
    path = serializers.CharField(max_length=255, min_length=4)
    company_id = serializers.IntegerField()
    created_by = serializers.IntegerField()
    last_edited_by = serializers.IntegerField()

    class Meta:
        model = Document
        fields = ['name', 'path', 'company_id','created_by', 'last_edited_by',]


    def validate(self, attrs):
        name = attrs.get('name', '')
        path = attrs.get('path', '')
        company_id = attrs.get('company_id', '')
        created_by = attrs.get('created_by', '')
        last_edited_by = attrs.get('last_edited_by', '')

        if name is None:
            raise serializers.ValidationError(
                {'name': ('Name cannot be empty')})
        if path is None:
            raise serializers.ValidationError(
                {'path': ('Path cannot be empty')})
        if company_id is None:
            raise serializers.ValidationError(
                {'company_id': ('company_id cannot be empty')})
        if created_by is None:
            raise serializers.ValidationError(
                {'created_by': ('created_by cannot be empty')})
        if last_edited_by is None:
            raise serializers.ValidationError(
                {'last_edited_by': ('last_edited_by cannot be empty')})
        
        return super().validate(attrs)

    def create(self, validated_data):
        
        return Document.objects.create_document(**validated_data)
        # creating_user = get_user_model().objects.get(id=validated_data.get('created_by'))
        # permission = DocumentPermission.objects.grant_basic_permissions(document_id= document, user_id= creating_user)
        # Document.grant_access(permissions=permission, document=document)

        #return document