# Generated by Django 2.1.4 on 2019-01-26 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20190126_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='qauntity',
            field=models.IntegerField(),
        ),
    ]
