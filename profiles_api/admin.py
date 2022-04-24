from django.contrib import admin
from profiles_api import models

admin.register(models.UserProfile)
admin.register(models.ProfileFeedItem)
