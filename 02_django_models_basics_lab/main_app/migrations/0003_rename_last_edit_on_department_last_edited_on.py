# Generated by Django 4.2.4 on 2023-10-30 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_department_last_edit_on'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='last_edit_on',
            new_name='last_edited_on',
        ),
    ]
