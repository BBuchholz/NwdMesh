# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-23 21:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20180129_1444'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='quotetagging',
            unique_together=set([('quote', 'tag')]),
        ),
    ]
