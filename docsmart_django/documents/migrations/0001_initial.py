# Generated by Django 3.1.7 on 2021-03-25 10:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company', '0002_auto_20210318_1328'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('path', models.CharField(max_length=255)),
                ('date_last_edited', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('company_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='company.company')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='creator', to=settings.AUTH_USER_MODEL)),
                ('last_edited_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Document',
                'verbose_name_plural': 'Documents',
            },
        ),
        migrations.CreateModel(
            name='DocumentPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('can_view', models.BooleanField(default=True, verbose_name='Can View')),
                ('can_edit', models.BooleanField(default=False, verbose_name='Can Edit')),
                ('can_delete', models.BooleanField(default=False, verbose_name='Can Delete')),
                ('document_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documents.document')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='permission_owner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'DocumentPermission',
                'verbose_name_plural': 'DocumentPermissions',
            },
        ),
        migrations.AddField(
            model_name='document',
            name='permissions',
            field=models.ManyToManyField(blank=True, to='documents.DocumentPermission', verbose_name='Permission'),
        ),
    ]
