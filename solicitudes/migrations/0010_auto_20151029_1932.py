# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0009_auto_20151029_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarios',
            name='comentario',
            field=models.TextField(default=datetime.datetime(2015, 10, 30, 0, 32, 48, 721281, tzinfo=utc), blank=True),
            preserve_default=False,
        ),
    ]
