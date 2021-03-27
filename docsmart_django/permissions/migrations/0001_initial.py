# Generated by Django 3.1.7 on 2021-03-26 08:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('documents', '0001_initial'),
    ]

    operations = [
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
    ]
