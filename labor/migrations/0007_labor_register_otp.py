# Generated by Django 5.0 on 2023-12-26 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labor', '0006_labor_register_credential_is_sent'),
    ]

    operations = [
        migrations.AddField(
            model_name='labor_register',
            name='otp',
            field=models.CharField(default='569864', max_length=50),
        ),
    ]
