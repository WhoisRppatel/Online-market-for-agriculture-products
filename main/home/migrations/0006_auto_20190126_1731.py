# Generated by Django 2.1.4 on 2019-01-26 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20190126_1727'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='qauntity',
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.FloatField(default=1.0),
        ),
    ]
