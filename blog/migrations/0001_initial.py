# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-10 12:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='NAME')),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='TITLE')),
                ('content', models.TextField(verbose_name='CONTENT')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='CREATED_TIME')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='UPDATE_TIME')),
                ('author', models.CharField(max_length=32, verbose_name='AUTHOR')),
                ('category', models.ManyToManyField(blank=True, to='blog.Category')),
            ],
        ),
    ]
