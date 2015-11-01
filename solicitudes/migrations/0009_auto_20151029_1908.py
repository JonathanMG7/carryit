# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0008_auto_20151029_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarios',
            name='guia',
            field=models.CharField(max_length=20),
        ),
    ]
