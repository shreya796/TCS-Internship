# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-07-14 04:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ComplaintsForum', '0002_auto_20170714_0424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='client_name',
            field=models.CharField(max_length=50),
        ),
    ]