# Generated by Django 2.2.3 on 2019-09-07 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_auto_20190907_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='setting',
            field=models.TextField(blank=True, default='{"clissh": [{"name": "securecrt", "path": "C:\\\\Program Files\\\\VanDyke Software\\\\Clients\\\\SecureCRT.exe", "args": "/T /N \\"{username}@{host}-{hostname}\\" /SSH2 /L {login_user} /PASSWORD {login_passwd} {login_host} /P {port}", "enable": true}, {"name": "xshell", "path": "C:\\\\Program Files (x86)\\\\NetSarang\\\\Xmanager Enterprise 5\\\\Xshell.exe", "args": "-newtab \\"{username}@{host}-{hostname}\\" -url ssh://{login_user}:{login_passwd}@{login_host}:{port}", "enable": false}, {"name": "putty", "path": "C:\\\\Users\\\\xx\\\\AppData\\\\Roaming\\\\TP4A\\\\Teleport-Assist\\\\tools\\\\putty\\\\putty.exe", "args": "-l {login_user} -pw {login_passwd} {login_host} -P {port}", "enable": false}], "clisftp": [{"name": "winscp", "path": "C:\\\\Program Files\\\\winscp\\\\WinSCP.exe", "args": "/sessionname=\\"{username}@{host}-{hostname}\\" {login_user}:{login_passwd}@{login_host}:{port}", "enable": true}]}', null=True, verbose_name='设置'),
        ),
    ]
