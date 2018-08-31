# Generated by Django 2.1 on 2018-08-25 07:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, upload_to='')),
                ('address', models.TextField(blank=True, max_length=1000, verbose_name='Address')),
                ('city', models.CharField(blank=True, max_length=33, verbose_name='City')),
                ('state', models.CharField(blank=True, max_length=33, verbose_name='State')),
                ('country', models.CharField(blank=True, max_length=33, verbose_name='Country')),
                ('user_prof', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
