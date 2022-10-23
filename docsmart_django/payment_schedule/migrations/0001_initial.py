# Generated by Django 3.1.7 on 2021-05-14 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(blank=True, max_length=500, verbose_name='item')),
                ('price', models.DecimalField(blank=True, decimal_places=3, max_digits=9, verbose_name='price')),
                ('start', models.DateTimeField(blank=True, verbose_name='start')),
                ('finish', models.DateTimeField(blank=True, verbose_name='finish')),
            ],
            options={
                'verbose_name': 'PaymentSchedule',
                'verbose_name_plural': 'PaymentSchedules',
            },
        ),
    ]
