# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-18 08:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsModel', '0009_site_crawl_deep'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='main_name',
            field=models.CharField(default=None, max_length=100, verbose_name='主站点名'),
        ),
    ]
