# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-14 07:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20160614_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='imgurl',
            field=models.CharField(default='a', max_length=100),
            preserve_default=False,
        ),
    ]
