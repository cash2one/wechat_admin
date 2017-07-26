# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 22:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WeChatModel', '0002_auto_20170725_2234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wechatuser',
            name='crawled',
        ),
        migrations.AddField(
            model_name='wechatuser',
            name='crawl_history',
            field=models.BooleanField(default=False, verbose_name='是否爬取历史文章'),
        ),
        migrations.AddField(
            model_name='wechatuser',
            name='crawled_history',
            field=models.BooleanField(default=False, verbose_name='是否爬取过历史文章'),
        ),
        migrations.AlterField(
            model_name='keyword',
            name='enable',
            field=models.BooleanField(default=True, verbose_name='是否启用'),
        ),
        migrations.AlterField(
            model_name='keyword',
            name='name',
            field=models.CharField(max_length=100, verbose_name='关键词'),
        ),
        migrations.AlterField(
            model_name='loginuser',
            name='enable',
            field=models.BooleanField(default=True, verbose_name='是否启用'),
        ),
        migrations.AlterField(
            model_name='loginuser',
            name='name',
            field=models.CharField(max_length=100, verbose_name='用户名'),
        ),
        migrations.AlterField(
            model_name='loginuser',
            name='password',
            field=models.CharField(max_length=100, verbose_name='密码'),
        ),
        migrations.AlterField(
            model_name='wechatdata',
            name='content',
            field=models.CharField(max_length=6000, verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='wechatdata',
            name='like_num',
            field=models.IntegerField(default=0, verbose_name='点赞数'),
        ),
        migrations.AlterField(
            model_name='wechatdata',
            name='read_num',
            field=models.IntegerField(default=0, verbose_name='阅读量'),
        ),
        migrations.AlterField(
            model_name='wechatdata',
            name='title',
            field=models.CharField(max_length=100, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='wechatdata',
            name='url',
            field=models.URLField(default=None, max_length=500, verbose_name='链接'),
        ),
        migrations.AlterField(
            model_name='wechatuser',
            name='alias',
            field=models.CharField(max_length=100, verbose_name='别名'),
        ),
        migrations.AlterField(
            model_name='wechatuser',
            name='description',
            field=models.CharField(default=None, max_length=255, verbose_name='描述'),
        ),
        migrations.AlterField(
            model_name='wechatuser',
            name='enable',
            field=models.BooleanField(default=True, verbose_name='是否启用'),
        ),
        migrations.AlterField(
            model_name='wechatuser',
            name='fakeid',
            field=models.CharField(default=None, max_length=100, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='wechatuser',
            name='monitored',
            field=models.BooleanField(default=False, verbose_name='是否监控最新文章'),
        ),
        migrations.AlterField(
            model_name='wechatuser',
            name='nickname',
            field=models.CharField(max_length=100, verbose_name='昵称'),
        ),
        migrations.AlterField(
            model_name='wechatuser',
            name='round_head_img',
            field=models.URLField(default=None, max_length=500, verbose_name='头像'),
        ),
        migrations.AlterField(
            model_name='wechatuser',
            name='service_type',
            field=models.IntegerField(default=1, verbose_name='服务类型'),
        ),
    ]
