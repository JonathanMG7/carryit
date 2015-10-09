# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='observaciones',
            field=models.TextField(null=True),
        ),
    ]
