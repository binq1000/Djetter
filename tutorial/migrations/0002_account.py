# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-22 10:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('bio', models.CharField(max_length=500)),
                ('following', models.ManyToManyField(blank=True, related_name='followers', to='tutorial.Account')),
            ],
        ),
    ]
