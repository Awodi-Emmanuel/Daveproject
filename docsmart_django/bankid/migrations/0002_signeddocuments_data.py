# Generated by Django 3.1.7 on 2021-05-10 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankid', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='signeddocuments',
            name='data',
            field=models.JSONField(null=True),
        ),
    ]
