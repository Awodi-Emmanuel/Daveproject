# Generated by Django 3.1.7 on 2021-05-05 14:57

from django.db import migrations, models
import plugins_base.models


class Migration(migrations.Migration):

    dependencies = [
        ('plugins_base', '0002_plugin_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plugin',
            name='app',
            field=models.CharField(choices=[(plugins_base.models.AppTypes['SALES'], 'Sales'), (plugins_base.models.AppTypes['HR'], 'Human resource'), (plugins_base.models.AppTypes['LEGAL'], 'Legal'), (plugins_base.models.AppTypes['GENERAL'], 'General')], max_length=100),
        ),
        migrations.AlterField(
            model_name='plugin',
            name='status',
            field=models.CharField(choices=[(plugins_base.models.STATUS['ACTIVE'], 'Active'), (plugins_base.models.STATUS['EXPIRED'], 'Expired'), (plugins_base.models.STATUS['TRIAL'], 'Trial'), (plugins_base.models.STATUS['EXTENSION'], 'Extension')], default=plugins_base.models.STATUS['TRIAL'], max_length=100),
        ),
    ]