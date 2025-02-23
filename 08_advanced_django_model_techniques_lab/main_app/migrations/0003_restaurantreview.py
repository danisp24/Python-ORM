# Generated by Django 4.2.4 on 2023-11-23 01:58

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_restaurant_location_menu'),
    ]

    operations = [
        migrations.CreateModel(
            name='RestaurantReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewer_name', models.CharField(max_length=100)),
                ('review_content', models.TextField()),
                ('rating', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(5)])),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.restaurant')),
            ],
            options={
                'verbose_name': 'Restaurant Review',
                'verbose_name_plural': 'Restaurant Reviews',
                'ordering': ('-rating',),
                'unique_together': {('reviewer_name', 'restaurant')},
            },
        ),
    ]
