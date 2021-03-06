# Generated by Django 2.1.4 on 2019-01-26 09:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0002_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('catagory', models.CharField(max_length=30, null=True)),
                ('description', models.CharField(max_length=100, null=True)),
                ('price', models.IntegerField()),
                ('pic_path', models.CharField(max_length=30, null=True)),
                ('status', models.BooleanField(default=False)),
                ('qauntity', models.FloatField()),
                ('time', models.DateTimeField()),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
