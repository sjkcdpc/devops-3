# Generated by Django 2.2.3 on 2019-09-23 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0002_auto_20190812_0922'),
    ]

    operations = [
        migrations.AddField(
            model_name='remoteuserbindhost',
            name='platform',
            field=models.SmallIntegerField(choices=[(1, 'linux'), (2, 'windows'), (3, 'unix')], default=1, verbose_name='平台'),
        ),
        migrations.CreateModel(
            name='ServerDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpu_model', models.CharField(blank=True, max_length=128, null=True, verbose_name='CPU型号')),
                ('cpu_number', models.SmallIntegerField(blank=True, null=True, verbose_name='物理CPU个数')),
                ('vcpu_number', models.SmallIntegerField(blank=True, null=True, verbose_name='逻辑CPU个数')),
                ('disk_total', models.CharField(blank=True, max_length=16, null=True, verbose_name='磁盘空间')),
                ('ram_total', models.SmallIntegerField(blank=True, null=True, verbose_name='内存容量')),
                ('kernel', models.CharField(blank=True, max_length=128, null=True, verbose_name='内核版本')),
                ('system', models.CharField(blank=True, max_length=128, null=True, verbose_name='操作系统')),
                ('filesystems', models.TextField(blank=True, null=True, verbose_name='文件系统')),
                ('interfaces', models.TextField(blank=True, null=True, verbose_name='网卡信息')),
                ('server', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='server.RemoteUserBindHost')),
            ],
            options={
                'verbose_name': '主机详细',
                'verbose_name_plural': '主机详细',
            },
        ),
    ]
