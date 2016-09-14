# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-14 00:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersistentStorage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application', models.CharField(max_length=63)),
                ('modelname', models.CharField(max_length=63)),
                ('inserted', models.DateTimeField(auto_now_add=True)),
                ('codec', models.CharField(max_length=128)),
                ('data', models.TextField()),
            ],
        ),
    ]
