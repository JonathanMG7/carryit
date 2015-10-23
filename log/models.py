from django.db import models
from django.contrib.auth.models import User

     
class UserProfile(models.Model):
	cedula = models.CharField(max_length=10, unique=True)
	home_address = models.TextField()
	phone_numer = models.CharField(max_length=20)
	user = models.OneToOneField(User)

	def get_guia(self):
		return self.cedula

	def save(self, *args, **kwargs):
		super(UserProfile, self).save(*args, **kwargs)

	def __unicode__(self):

		return self.cedula