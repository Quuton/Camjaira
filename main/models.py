from django.db import models

# Create your models here.

class Room(models.Model):
    # Information provided by the owner
    number = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    floor = models.IntegerField()
    type = models.CharField(max_length=50)
    image = models.ImageField(upload_to='room_images',blank=True, default='room_images/placeholder.png')
    size = models.IntegerField()
    price = models.FloatField()
    availability = models.BooleanField(default=True)

    # Fields handled by the server
    visitCount = models.IntegerField(default=0)
    lastUpdated = models.DateTimeField(auto_now = True)

class Appointment(models.Model):
    # Information the visitor submits
    name = models.CharField(max_length=200)
    email = models.EmailField()
    topic = models.CharField(max_length=50)
    message = models.TextField()

    # Fields handled by the server
    ipAddress = models.GenericIPAddressField()
    timeStamp = models.DateTimeField(auto_now = True)
    resolved = models.BooleanField(default = False)