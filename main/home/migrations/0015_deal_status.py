# Generated by Django 2.1.7 on 2019-03-10 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_deal_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='deal',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
