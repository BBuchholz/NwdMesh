# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-08 21:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_quoteaccesslogentry'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quoteaccesslogentry',
            name='quote',
        ),
        migrations.RemoveField(
            model_name='quoteaccesslogentry',
            name='user',
        ),
        migrations.AddField(
            model_name='quote',
            name='last_accessed',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.DeleteModel(
            name='QuoteAccessLogEntry',
        ),
    ]
