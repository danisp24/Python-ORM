# Generated by Django 4.2.4 on 2023-11-06 11:44

from django.db import migrations


def create_unique_brands(apps, schema_editor):
    Shoe = apps.get_model('main_app', 'Shoe')
    Unique_brands = apps.get_model('main_app', 'UniqueBrands')

    unique_brand_names = Shoe.objects.values_list('brand', flat=True).distinct()

    unique_brands_to_create = [Unique_brands(brand_name=brand_name) for brand_name in unique_brand_names]

    Unique_brands.objects.bulk_create(unique_brands_to_create)


def delete_unique_brands(apps, schema_editor):
    Unique_brands = apps.get_model('main_app', 'UniqueBrands')
    Unique_brands.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_uniquebrands'),
    ]

    operations = [migrations.RunPython(create_unique_brands, reverse_code=delete_unique_brands)
    ]
