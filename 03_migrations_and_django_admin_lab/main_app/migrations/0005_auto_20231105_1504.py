# Generated by Django 4.2.4 on 2023-11-05 12:37
import random

from django.db import migrations


def add_barcode(apps, schema_editor):
    Product = apps.get_model('main_app', 'Product')
    products = Product.objects.all()
    all_barcodes = random.sample(
        range(100000000, 999999999),
        len(products)
    )

    for i in range(len(products)):
        product = products[i]
        product.barcode = all_barcodes[i]
        product.save()


def reverse_add_barcode(apps, schema_editor):
    Product = apps.get_model('main_app', 'Product')


class Migration(migrations.Migration):
    dependencies = [
        ('main_app', '0004_product_barcode'),
    ]

    operations = [migrations.RunPython(add_barcode, reverse_code=reverse_add_barcode)
                  ]

