# Generated by Django 3.0 on 2020-02-02 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jifenpay',
            name='pay_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='付款时间'),
        ),
    ]
