# Generated by Django 2.0.7 on 2019-06-26 02:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tourism', '0014_hotels_star'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotels',
            name='image',
        ),
    ]