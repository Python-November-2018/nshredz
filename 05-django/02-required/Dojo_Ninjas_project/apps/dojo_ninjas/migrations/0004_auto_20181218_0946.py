# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-12-18 15:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas', '0003_auto_20181218_0945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ninja',
            name='dojo',
        ),
        migrations.DeleteModel(
            name='Dojo',
        ),
        migrations.DeleteModel(
            name='Ninja',
        ),
    ]
