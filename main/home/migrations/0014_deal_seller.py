# Generated by Django 2.1.7 on 2019-03-06 11:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0013_merge_20190306_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='deal',
            name='seller',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seller_name', to=settings.AUTH_USER_MODEL),
        ),
    ]
