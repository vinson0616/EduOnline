# Generated by Django 3.0 on 2020-02-02 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_jifenpay_pay_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='jifenpay',
            name='total_jifen',
            field=models.IntegerField(default=0, verbose_name='交易积分'),
        ),
    ]