# Generated by Django 4.2.4 on 2023-10-30 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='last_edit_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
