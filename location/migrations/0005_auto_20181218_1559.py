# Generated by Django 2.1 on 2018-12-18 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0004_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placemap',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.Location'),
        ),
    ]
