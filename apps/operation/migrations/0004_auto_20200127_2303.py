# Generated by Django 3.0 on 2020-01-27 23:03

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('operation', '0003_auto_20200127_2302'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserJifenDetail1',
            new_name='UserJifenDetail',
        ),
    ]