# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-19 09:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_paper_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='abstract',
            field=models.CharField(max_length=256, null=True, verbose_name='ABSTRACT'),
        ),
    ]