# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0004_solicitud_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitud',
            name='guia',
            field=models.CharField(default='Null', max_length=20),
            preserve_default=False,
        ),
    ]
