from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Room)
admin.site.register(models.Appointment)
admin.site.register(models.Suggestion)
admin.site.register(models.Review)
admin.site.register(models.RoomAmenity)
admin.site.register(models.UserProfile)