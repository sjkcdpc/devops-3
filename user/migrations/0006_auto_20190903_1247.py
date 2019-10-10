# Generated by Django 2.2.3 on 2019-09-03 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20190816_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginlog',
            name='event_type',
            field=models.SmallIntegerField(choices=[(1, '登陆'), (2, '退出'), (3, '登陆错误'), (4, '修改密码失败'), (5, '修改密码成功'), (6, '添加用户'), (7, '删除用户'), (8, '添加组'), (9, '删除组'), (10, '更新用户'), (11, '更新组'), (12, '添加主机'), (13, '删除主机'), (14, '更新主机'), (15, '添加主机用户'), (16, '删除主机用户'), (17, '更新主机用户'), (18, '停止在线会话'), (19, '锁定在线会话')], default=1, verbose_name='事件类型'),
        ),
    ]
