# Generated by Django 3.0.5 on 2020-06-12 14:21

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockbuddy', '0010_auto_20200612_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockdata',
            name='mlprediction',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, default='0', null=True), null=True, size=None),
        ),
    ]