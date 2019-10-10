# Generated by Django 2.2.3 on 2019-08-26 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webssh', '0005_auto_20190816_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='terminalsession',
            name='type',
            field=models.SmallIntegerField(choices=[(1, 'webssh'), (2, 'websftp'), (3, 'clissh'), (4, 'clisftp'), (5, 'webtelnet'), (6, 'clitelnet')], default=1, verbose_name='类型'),
        ),
    ]
