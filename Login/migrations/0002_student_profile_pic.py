# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-10 00:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
