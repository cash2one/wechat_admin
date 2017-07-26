# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 23:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WeChatModel', '0003_auto_20170725_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyword',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='关键词'),
        ),
        migrations.AlterField(
            model_name='loginuser',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='用户名'),
        ),
        migrations.AlterField(
            model_name='wechatdata',
            name='content',
            field=models.TextField(verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='wechatdata',
            name='pub_time',
            field=models.DateTimeField(default=None, verbose_name='发布时间'),
        ),
        migrations.AlterField(
            model_name='wechatdata',
            name='url',
            field=models.URLField(default=None, max_length=255, unique=True, verbose_name='链接'),
        ),
        migrations.AlterField(
            model_name='wechatuser',
            name='alias',
            field=models.CharField(max_length=100, unique=True, verbose_name='别名'),
        ),
        migrations.AlterField(
            model_name='wechatuser',
            name='fakeid',
            field=models.CharField(default=None, max_length=100, unique=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='wechatuser',
            name='nickname',
            field=models.CharField(max_length=100, unique=True, verbose_name='昵称'),
        ),
    ]
