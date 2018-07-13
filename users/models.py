from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name='手机号码')
    image = models.ImageField(upload_to='images/%Y/%m/%d/', default='images/default.png', max_length=100)

    class Meta:
        db_table = 'ops_user'
        verbose_name = '用户表'
        verbose_name_plural = '用户表'


class UserLog(models.Model):
    user = models.CharField(max_length=16, verbose_name='操作用户')
    remote_ip = models.GenericIPAddressField(verbose_name='操作用户IP')
    content = models.CharField(max_length=100, verbose_name='操作内容')
    c_time = models.DateTimeField(auto_now_add=True, verbose_name='操作时间')


class UserPlan(models.Model):
    title = models.CharField(max_length=32, verbose_name='计划标题')
    start_time = models.DateTimeField(null=True, blank=True, verbose_name='开始时间')
    end_time = models.DateTimeField(null=True, blank=True, verbose_name='结束时间')
    all_day = models.SmallIntegerField(null=True, blank=True, verbose_name='是否全天')
    color = models.CharField(null=True, blank=True, max_length=32, verbose_name='颜色')
