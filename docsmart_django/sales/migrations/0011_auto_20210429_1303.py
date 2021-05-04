# Generated by Django 3.1.7 on 2021-04-29 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_auto_20210421_1044'),
        ('sales', '0010_auto_20210428_1538'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sales',
            name='company',
        ),
        migrations.AddField(
            model_name='sales',
            name='related_company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='company.company'),
            preserve_default=False,
        ),
    ]