from django.contrib import admin

from log.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
	list_display = ['cedula', 'home_address', 'phone_numer', 'user']


admin.site.register(UserProfile, UserProfileAdmin)

