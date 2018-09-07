from django.db import models


class FortServer(models.Model):
    server_status_ = (
        (0, '禁用'),
        (1, '正常'),
    )
    server = models.OneToOneField('assets.ServerAssets', on_delete=models.CASCADE)
    server_status = models.SmallIntegerField(choices=server_status_, default=1, verbose_name='是否允许web登录')

    class Meta:
        db_table = 'ops_fort_server'
        permissions = (
            ("view_fortserver", "读取堡垒机权限"),
            ("ssh_fortserver", "连接主机权限"),
        )
        verbose_name = '堡垒机表'
        verbose_name_plural = '堡垒机表'


class FortServerUser(models.Model):
    fort_user_status_ = (
        (0, '禁用'),
        (1, '正常')
    )
    auth_types = (
        (0, '账户密码'),
        (1, '密钥认证'),
    )
    fort_server = models.ForeignKey('FortServer', on_delete=models.CASCADE)
    fort_username = models.CharField(max_length=64, verbose_name='登录用户')
    fort_password = models.CharField(max_length=64, null=True, blank=True, verbose_name='登录密码')
    fort_user_status = models.SmallIntegerField(choices=fort_user_status_, default=1, verbose_name='用户状态')
    fort_auth_type = models.SmallIntegerField(choices=auth_types, default=0, verbose_name='认证方式')
    fort_key_file = models.TextField(null=True, blank=True, verbose_name='私钥内容')
    fort_belong_user = models.ManyToManyField('users.UserProfile', blank=True, verbose_name='所属用户')
    fort_belong_group = models.ManyToManyField('auth.Group', blank=True, verbose_name='所属组')
    fort_user_memo = models.TextField(null=True, blank=True, verbose_name='用户说明')

    class Meta:
        db_table = 'ops_fort_user'
        verbose_name = '堡垒机用户表'
        verbose_name_plural = '堡垒机用户表'


class FortRecord(models.Model):
    login_user = models.ForeignKey('users.UserProfile', verbose_name='用户', on_delete=models.CASCADE)
    fort = models.CharField(max_length=32, verbose_name='登录主机及用户')
    remote_ip = models.GenericIPAddressField(verbose_name='远程地址')
    start_time = models.CharField(max_length=64, verbose_name='开始时间')
    login_status_time = models.CharField(max_length=16, verbose_name='登录时长')
    record_file = models.CharField(max_length=256, verbose_name='操作记录')

    class Meta:
        db_table = 'ops_fort_record'
        verbose_name = '操作记录表'
        verbose_name_plural = '操作记录表'
