# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('solicitudes', '0006_auto_20151023_1331'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(auto_now_add=True, max_length=15)),
                ('comentario', models.TextField(null=True, blank=True)),
                ('guia', models.OneToOneField(related_name='coment', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
