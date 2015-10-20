# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sms',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('number', models.CharField(max_length=32)),
                ('vcode', models.IntegerField(null=True)),
            ],
        ),
    ]
