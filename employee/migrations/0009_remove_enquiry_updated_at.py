# Generated by Django 5.1.4 on 2024-12-23 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0008_enquiry'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enquiry',
            name='updated_at',
        ),
    ]