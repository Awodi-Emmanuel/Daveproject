# Generated by Django 3.1.7 on 2021-05-10 01:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0003_auto_20210507_1640'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscription',
            old_name='user',
            new_name='company',
        ),
    ]