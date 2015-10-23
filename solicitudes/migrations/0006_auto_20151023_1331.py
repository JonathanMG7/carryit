# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0005_solicitud_guia'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitud',
            name='mensajero',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, max_length=15),
        ),
    ]
