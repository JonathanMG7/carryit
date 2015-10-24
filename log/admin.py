from django.contrib import admin

from log.models import Profile


class ProfileAdmin(admin.ModelAdmin):
	list_display = ['cedula', 'home_address', 'phone_numer', 'user']


admin.site.register(Profile, ProfileAdmin)

