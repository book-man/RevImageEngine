# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-03 08:22
from __future__ import unicode_literals

from django.db import migrations
import picklefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('image_match', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='features',
            field=picklefield.fields.PickledObjectField(default=0, editable=False),
        ),
    ]
