# Generated by Django 3.0.4 on 2020-08-07 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(default='media/news/Camping.jpg', upload_to='media/items'),
        ),
    ]