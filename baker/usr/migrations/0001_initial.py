# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=64, db_index=True)),
                ('avatar', models.CharField(max_length=256)),
                ('signature', models.CharField(max_length=256)),
                ('created', models.DateTimeField(auto_now=True)),
                ('sex', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='VCode',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('number', models.BigIntegerField(unique=True)),
            ],
        ),
    ]
