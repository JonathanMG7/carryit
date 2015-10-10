# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0003_auto_20151008_2139'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitud',
            name='estado',
            field=models.CharField(default=b'PENDIENTE', max_length=20, choices=[(b'PENDIENTE', b'Pendiente'), (b'EN_PROCESO', b'En proceso'), (b'ENTREGADO', b'Entregado')]),
        ),
    ]
