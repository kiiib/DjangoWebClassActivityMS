# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-14 06:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_activity_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='title',
            field=models.CharField(default='test', max_length=20),
            preserve_default=False,
        ),
    ]