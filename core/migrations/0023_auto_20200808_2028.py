# Generated by Django 3.0.4 on 2020-08-08 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_auto_20200808_1605'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='title_Voxa',
            new_name='title',
        ),
    ]
