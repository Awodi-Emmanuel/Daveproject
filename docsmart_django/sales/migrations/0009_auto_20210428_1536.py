# Generated by Django 3.1.7 on 2021-04-28 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0008_auto_20210428_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='total',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=9, null=True),
        ),
    ]
