# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-18 15:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='mobile',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='手机号码'),
        ),
        migrations.AddField(
            model_name='user',
            name='qq',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='qq号码'),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, default='./avatar/boy.jpg', max_length=200, null=True, upload_to='./avatar/%Y/%m', verbose_name='用户头像'),
        ),
    ]
