# Generated by Django 3.1.4 on 2021-01-20 13:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('coremetric_app', '0002_auto_20210120_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='commentedOn',
            field=models.DateField(verbose_name=datetime.datetime(2021, 1, 20, 13, 26, 37, 605373, tzinfo=utc)),
        ),
    ]
