from django.contrib.auth import get_user_model
from permissions.models import DocumentPermission
from rest_framework import serializers
from .models import Document


class DocumentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        max_length=255, min_length=8)
    path = serializers.CharField(max_length=255, min_length=4)
    content = serializers.CharField(required=False)
    company_id = serializers.CharField(required=False)
    created_by = serializers.CharField()

    class Meta:
        model = Document
        fields = ['name', 'path', 'content', 'company_id', 'created_by']

    def validate(self, attrs):
        name = attrs.get('name', '')
        path = attrs.get('path', '')
        created_by = attrs.get('created_by', '')

        if name is None:
            raise serializers.ValidationError(
                {'name': 'Name cannot be empty'})
        if path is None:
            raise serializers.ValidationError(
                {'path': 'Path cannot be empty'})
        if created_by is None:
            raise serializers.ValidationError(
                {'created_by': 'created_by cannot be empty'})

        return super().validate(attrs)

    def create(self, validated_data):
        document = Document.objects.create_document(**validated_data)
        user = get_user_model().objects.get(id=validated_data.get('created_by'))
        permission = DocumentPermission.objects.grant_basic_permissions(document_id=document, user_id=user)
        Document.grant_access(permissions=permission, document=document)
        return document


class FetchSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentPermission
        depth = 1
        fields = ['document_id', 'can_view', 'can_edit', 'can_delete', ]


class FetchUserDocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        depth = 1
        fields = ['id', 'name', 'path', 'content', 'date_last_edited', 'created_at',
                  'updated_at', 'date_last_edited', 'permissions']
