# Generated by Django 3.0 on 2020-02-01 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0007_auto_20200128_0018'),
    ]

    operations = [
        migrations.AddField(
            model_name='jifendetail',
            name='desc',
            field=models.CharField(default='', max_length=300, verbose_name='积分说明'),
        ),
    ]