# Generated by Django 3.1.7 on 2021-05-14 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VAT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='Name')),
                ('rate', models.DecimalField(decimal_places=3, max_digits=9, verbose_name='Rate')),
                ('percentage', models.DecimalField(decimal_places=3, max_digits=9, verbose_name='Percentage')),
            ],
            options={
                'verbose_name': 'VAT',
                'verbose_name_plural': 'VATs',
            },
        ),
    ]
