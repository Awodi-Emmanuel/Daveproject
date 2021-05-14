# Generated by Django 3.1.7 on 2021-05-14 11:12

from django.db import migrations, models
import django.db.models.deletion
import roles.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[(roles.models.Roles['OWNER'], 'Owner'), (roles.models.Roles['ADMIN'], 'Admin'), (roles.models.Roles['EMPLOYEE'], 'Employee')], max_length=5)),
                ('company', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='company.company')),
            ],
            options={
                'verbose_name': 'Role',
                'verbose_name_plural': 'Roles',
            },
        ),
    ]
