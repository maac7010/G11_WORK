# Generated by Django 5.2.3 on 2025-06-25 08:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labor', '0008_labor_register_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labor_register',
            name='start_date',
            field=models.DateTimeField(default=datetime.date.today),
        ),
    ]
