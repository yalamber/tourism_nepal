# Generated by Django 2.0.7 on 2019-06-17 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourism', '0004_auto_20190616_1901'),
    ]

    operations = [
        migrations.AddField(
            model_name='attractions',
            name='latitude',
            field=models.FloatField(default=27.489595),
        ),
        migrations.AddField(
            model_name='attractions',
            name='longitude',
            field=models.FloatField(default=83.277083),
        ),
    ]
