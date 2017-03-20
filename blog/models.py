# coding:utf-8
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
# blog数据库所需要的表
# 个人记录生活的博客
# 用户表
# 标签 一篇文章可以有很多标签 一个标签也可以为很多文章拥有
# 文章分类
# 文章模型
# 评论模型 （别人访问）
# 广告模型 （这个可以先不用）

class User(AbstractUser):
    # 头像已经上传成功了 然后怎么通过默认添加图片(默认图片是添加图片的路径吗 这就有点意思了) 怎么通过性别来默认图片的加载呢
    # 图片上传成功后 怎么用又是另外一回事了(能不能成功取出来)
    avatar = models.ImageField(upload_to='./avatar/%Y/%m',default='./avatar/boy.jpg',max_length=200,blank=True,null=True,verbose_name="用户头像")
    qq = models.CharField(max_length=20,blank=True,null=True,verbose_name='qq号码')
    # 输入"    "能不能输入成功 或 不输入能不能成功
    # blank = False -- 不能输入空格符号
    mobile = models.CharField(max_length=11,blank=False,null=True,verbose_name='手机号码')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name


# 标签
class Tag(models.Model):
    name = models.CharField(max_length=30,verbose_name="标签名称")

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name

    '''python3用__str__返回字符串 用__unicode__就不行了'''
    def __str__(self):
        return self.name

# 文章分类
class Category(models.Model):
    name = models.CharField(max_length=30,verbose_name="分类名称")

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# 文章模型
# 文章需要什么字段
# title 描述 正文 作者 分类 标签 日期 用户 点击次数 特别喜欢
class Article(models.Model):
    title = models.CharField(max_length=50,verbose_name='文章标题')
    desc = models.CharField(max_length=50,verbose_name='文章描述')
    content = models.TextField(verbose_name='文章内容')
    click_count = models.IntegerField(default=0,verbose_name='点击次数')
    is_love = models.BooleanField(default=False,verbose_name='特别喜欢')
    # auto_now_add 关于时间这个字段
    date_publish = models.DateTimeField(auto_now_add=True,verbose_name='发布时间')

    user = models.ForeignKey(User,verbose_name='用户')
    # 外键与多对一的区别
    category = models.ForeignKey(Category,verbose_name='分类')
    tag = models.ManyToManyField(Tag,verbose_name='标签')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title



