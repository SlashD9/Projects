# Generated by Django 5.2.3 on 2025-06-25 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workforms', '0012_remove_worksheet_customer_signature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='worksheet',
            name='date',
            field=models.DateField(),
        ),
    ]
