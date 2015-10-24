# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    cedula = models.CharField(max_length=10, unique=True)
    home_address = models.CharField(max_length=50)
    phone_numer = models.CharField(max_length=20)
    user = models.OneToOneField(User, related_name='prof')

    def get_guia(self):
        return self.cedula

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

    def __unicode__(self):

        return self.cedula
