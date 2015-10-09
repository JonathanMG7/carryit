# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(default=b'ENCOMIENDA', max_length=20, choices=[(b'ENCOMIENDA', b'Encomienda'), (b'TRAMITE', b'Tramite')])),
                ('dir_origen', models.CharField(max_length=200)),
                ('dir_destino', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('observaciones', models.TextField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
