# Generated by Django 3.1.4 on 2021-01-20 13:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
                ('comment', models.TextField()),
                ('commentedOn', models.DateField(verbose_name=datetime.datetime(2021, 1, 20, 13, 24, 12, 619857, tzinfo=utc))),
            ],
        ),
    ]
