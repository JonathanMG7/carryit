# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0007_comentarios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarios',
            name='guia',
            field=models.OneToOneField(related_name='coment', to='solicitudes.Solicitud'),
        ),
    ]
