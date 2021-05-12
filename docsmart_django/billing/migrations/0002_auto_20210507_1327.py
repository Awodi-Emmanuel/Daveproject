# Generated by Django 3.1.7 on 2021-05-07 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('billing', '0001_initial'),
        ('company', '0005_company_company_size'),
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='payment',
            field=models.OneToOneField(blank=True, db_column='payment', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='payments.payment'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='plan',
            field=models.ForeignKey(blank=True, db_column='plan', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='billing.billingplans'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='user',
            field=models.ForeignKey(blank=True, db_column='company', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='company.company'),
        ),
    ]