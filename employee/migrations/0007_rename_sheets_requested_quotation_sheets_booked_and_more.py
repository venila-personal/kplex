# Generated by Django 5.1.4 on 2024-12-17 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0006_quotation_final_price_with_gst'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quotation',
            old_name='sheets_requested',
            new_name='sheets_booked',
        ),
        migrations.RemoveField(
            model_name='quotation',
            name='final_price_with_gst',
        ),
        migrations.RemoveField(
            model_name='quotation',
            name='igst',
        ),
        migrations.RemoveField(
            model_name='quotation',
            name='remarks',
        ),
        migrations.RemoveField(
            model_name='quotation',
            name='sgst',
        ),
        migrations.AddField(
            model_name='quotation',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
