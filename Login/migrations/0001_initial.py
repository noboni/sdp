# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 06:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('user_id', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=250)),
                ('mail_id', models.CharField(max_length=250)),
                ('dob', models.CharField(max_length=250)),
                ('batch', models.CharField(max_length=250)),
            ],
        ),
    ]