# coding:utf-8
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# 标签
class Tag(models.Model):
    name = models.CharField(max_length=30,verbose_name='标签名称')

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __Unicode__(self):
        return self.name

#分类
class Category(models.Model):
    name = models.CharField(max_length=30,verbose_name='分类名称')
    index = models.IntegerField(default=999,verbose_name='分类的排序')

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __Unicode__(self):
        return self.name

# User
# 采用继承的方式扩展用户信息
# 采用关联的方式扩展...
# 继承AbstractUser的model 同步化的时候会出错
# 在setting.py上添加上 AUTH_USER_MODEL = 'cblog.User' app+继承的model
class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/%Y/%m', default='avatar/default.png', max_length=200, blank=True, null=True, verbose_name='用户头像')
    qq = models.CharField(max_length=20, blank=True, null=True, verbose_name='QQ号码')
    mobile = models.CharField(max_length=11, blank=True, null=True, unique=True, verbose_name='手机号码')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __unicode__(self):
        return self.username
