from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Room(models.Model):
    # Information provided by the owner
    number = models.CharField(max_length=20)
    description = models.TextField(blank = True)
    floor = models.IntegerField()
    type = models.CharField(max_length=50)
    image = models.ImageField(upload_to='room_images',blank = True, default='room_images/placeholder.png')
    size = models.IntegerField()
    price = models.FloatField()
    availability = models.BooleanField(default = True)

    # Fields handled by the server
    visitCount = models.IntegerField(default = 0)
    lastUpdated = models.DateTimeField(auto_now = True)

class RoomAmenity(models.Model):
    roomID = models.ForeignKey(Room, on_delete=models.CASCADE)
    name = models.CharField(max_length = 50)
    description = models.TextField(blank = True)

class Appointment(models.Model):
    # Information the visitor submits
    name = models.CharField(max_length=200)
    email = models.EmailField()
    scheduledDate = models.DateField()
    topic = models.CharField(max_length=50)
    message = models.TextField(blank = True)
    

    # Fields initialized by the server
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    ipAddress = models.GenericIPAddressField()
    timeStamp = models.DateTimeField(auto_now = True)
    resolved = models.BooleanField(default = False)

class Review(models.Model):
    cleanlinessRating = models.IntegerField()
    aestheticRating = models.IntegerField()
    comfortRating = models.IntegerField()
    valueRating = models.IntegerField()

    comment = models.TextField(blank = True)

    # Fields initialized by the server
    roomID = models.ForeignKey(Room, on_delete=models.CASCADE)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    timeStamp = models.DateTimeField(auto_now = True)

class Suggestion(models.Model):
    topic = models.CharField(max_length=50)
    message = models.TextField(blank = True)

    # Fields initialized by the server
    favourite = models.BooleanField(default = False)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    timeStamp = models.DateTimeField(auto_now = True)
    resolved = models.BooleanField(default = False)
