# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-08 22:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170508_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='premier-article-de-cecile', max_length=100),
            preserve_default=False,
        ),
    ]
