# Generated by Django 3.0 on 2020-02-01 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_auto_20200201_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='notice',
            field=models.CharField(default='', max_length=300, verbose_name='课程公告'),
        ),
    ]
