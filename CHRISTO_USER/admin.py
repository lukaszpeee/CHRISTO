from django.contrib import admin
from .models import UserProfile, TwitterProfile, TwitterProfilesList


admin.site.register(UserProfile)
admin.site.register(TwitterProfile)
admin.site.register(TwitterProfilesList)
