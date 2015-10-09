# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0002_auto_20151008_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitud',
            name='id_cliente',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='solicitud',
            name='nom_cliente',
            field=models.CharField(default='Nombre', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='solicitud',
            name='tel_cliente',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='observaciones',
            field=models.TextField(null=True, blank=True),
        ),
    ]
