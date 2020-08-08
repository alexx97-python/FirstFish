# Generated by Django 3.0.4 on 2020-08-07 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20200730_1146'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('category',)},
        ),
        migrations.AddField(
            model_name='item',
            name='colour',
            field=models.CharField(choices=[('BL', 'Black'), ('BW', 'Brown'), ('Gy', 'Gray'), ('Y', 'Yellow'), ('R', 'Red'), ('O', 'Orange'), ('B', 'Blue'), ('G', 'Grin')], default='BL', max_length=2),
        ),
        migrations.AddField(
            model_name='item',
            name='length',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='weight',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('SP', 'Spining'), ('FD', 'Feeder'), ('FL', 'Float'), ('WN', 'Winter'), ('SA', 'Sea'), ('CR', 'Carp'), ('TR', 'Tourism'), ('EQ', 'Equipment')], max_length=2),
        ),
    ]
