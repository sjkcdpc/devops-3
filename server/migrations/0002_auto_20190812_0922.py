# Generated by Django 2.2.3 on 2019-08-12 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remoteuserbindhost',
            name='env',
            field=models.SmallIntegerField(choices=[(1, '正式环境'), (2, '测试环境')], default=1, verbose_name='环境'),
        ),
        migrations.AlterField(
            model_name='remoteuserbindhost',
            name='protocol',
            field=models.SmallIntegerField(choices=[(1, 'ssh'), (2, 'telnet'), (3, 'rdp'), (4, 'vnc'), (5, 'sftp'), (6, 'ftp')], default=1, verbose_name='协议'),
        ),
        migrations.AlterField(
            model_name='remoteuserbindhost',
            name='type',
            field=models.SmallIntegerField(choices=[(1, '服务器'), (2, '防火墙'), (3, '路由器'), (4, '二层交换机'), (5, '三层交换机'), (6, '虚拟机'), (7, 'PC机')], default=1, verbose_name='类型'),
        ),
    ]
