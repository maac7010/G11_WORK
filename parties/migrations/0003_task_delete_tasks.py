# Generated by Django 5.0 on 2024-01-02 06:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parties', '0002_tasks'),
    ]

    operations = [
        migrations.CreateModel(
            name='task',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('task_id', models.CharField(blank=True, max_length=50, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('total_payment', models.FloatField()),
                ('task_status', models.CharField(blank=True, choices=[('Pending', 'Task Pending'), ('Ongoing', 'Task On-Going'), ('Done', 'Task Done')], default='Pending', max_length=50)),
                ('paid_payment', models.FloatField(blank=True, default=0)),
                ('payment_status', models.CharField(blank=True, choices=[('Pending', 'Payment Pending'), ('Done', 'Payment Done'), ('Partially Paid', 'Partially Paid')], default='Pending', max_length=50)),
                ('party_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parties.parties_detail')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='tasks',
        ),
    ]
