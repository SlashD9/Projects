# Generated by Django 5.2.3 on 2025-06-16 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workforms', '0006_stock_cost_price_stock_sales_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock',
            old_name='sales_price',
            new_name='sale_price',
        ),
    ]
