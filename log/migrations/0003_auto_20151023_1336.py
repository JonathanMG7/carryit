# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0002_auto_20151023_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='cedula',
            field=models.CharField(unique=True, max_length=10),
        ),
    ]
