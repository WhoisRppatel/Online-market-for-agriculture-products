# Generated by Django 2.1.4 on 2019-01-26 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20190124_2154'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='name',
            field=models.CharField(default='anything', max_length=20),
        ),
    ]