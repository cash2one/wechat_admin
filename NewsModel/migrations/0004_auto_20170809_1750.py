# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-09 09:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsModel', '0003_auto_20170809_1457'),
    ]

    operations = [
        migrations.RenameField(
            model_name='site',
            old_name='url_rule',
            new_name='url_rule_reg',
        ),
        migrations.AddField(
            model_name='site',
            name='url_rule_css',
            field=models.CharField(default=None, max_length=255, verbose_name='url css '),
        ),
        migrations.AddField(
            model_name='site',
            name='url_rule_xpath',
            field=models.CharField(default=None, max_length=255, verbose_name='url xpath '),
        ),
    ]
