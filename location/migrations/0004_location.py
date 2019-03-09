# Generated by Django 2.1 on 2018-12-17 17:44

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0003_auto_20181111_1902'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat_long', django.contrib.gis.db.models.fields.PointField(geography=True, null=True, srid=4326)),
            ],
        ),
    ]
