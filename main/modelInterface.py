# Handles direct transactions between the DB
from .models import *
import random
import itertools as it
from django.contrib.auth.models import Group
from django.db.models import Avg
def generateRoomData(n:int):
    for i in range(0,n):
        newRoomObj = Room(number = 'testobj' + str(i), description = 'Test description', floor = i, image = 'room_images/Draco.png', size = random.randint(0,200), price = random.randint(0,2000), availability = True, type = 'Single')
        newRoomObj.save()
    for i in range(0,n):
        newRoomObj = Room(number = 'testobj' + str(i), description = 'Test description', floor = i, image = 'room_images/Draco.png', size = random.randint(0,200), price = random.randint(0,2000), availability = True, type = 'Studio')
        newRoomObj.save()

def getRecentPosts(max_posts:int = 4):
    lastUpdatedRooms = Room.objects.order_by('-lastUpdated')[:max_posts]
    return lastUpdatedRooms

def getFeaturedRooms(max_posts:int = 8):
    studioRooms = Room.objects.filter(type__iexact = 'Studio').order_by('-visitCount')[:max_posts]
    singleBedRooms = Room.objects.filter(type__iexact = 'Single').order_by('-visitCount')[:max_posts]
    return {
        'studio':studioRooms,
        'single':singleBedRooms, 
        'studioChunkLimit':(studioRooms.count() - (studioRooms.count() % 4)),
        'singleChunkLimit':(singleBedRooms.count() - (singleBedRooms.count() % 4)),
        'studioMod':(studioRooms.count() % 4),
        'singleMod':(singleBedRooms.count() % 4),}


def getRooms(queryData:dict = None):
    querySet = None
    if queryData['orderDirection']:
        querySet = Room.objects.all().order_by(queryData['orderField'])
    else:
        querySet = Room.objects.all().order_by('-' + queryData['orderField'])
    
    # If for whatever goddamn reason or magic query is None instead of an empty string, this prevents that
    if queryData['query'] == None:
        queryData['query'] = ''

    if queryData['query'] != '':
        if queryData['queryType'] == 'type':
            querySet = querySet.filter(type = queryData['query'])
        elif queryData['queryType'] == 'description':
            querySet = querySet.filter(description__contains = queryData['query'])
        elif queryData['queryType'] == 'number':
            querySet = querySet.filter(number = queryData['query'])
    

    querySet = querySet.filter(price__gte = queryData['priceMin'])


    if queryData['priceMax'] != 0:
        querySet = querySet.filter(price__lte = queryData['priceMax'])
        
    return querySet

        

def getRoom(id:int):
    temp = Room.objects.get(id = id)
    temp.visitCount += 1
    temp.save()
    
    return Room.objects.get(id = id)

def saveRoomRecord(data:dict, id:int = None):
    if id == None:
        RoomObject = Room ( 
            number = data.get('number'),
            description = data.get('description', ''),
            price = data.get('price', 0),
            size = data.get('size', 0),
            type = data.get('type', 'Studio'),
            floor = data.get('floor', 1),
            availability = data.get('availability', True),
            image = data.get('image'))
    else:
        try:
            RoomObject = Room.objects.get(id = id)
            RoomObject.number = data.get('number', RoomObject.number)
            RoomObject.description = data.get('description', RoomObject.description)
            RoomObject.price = data.get('price', RoomObject.price)
            RoomObject.size = data.get('size', RoomObject.size)
            RoomObject.type = data.get('type', RoomObject.type)
            RoomObject.floor = data.get('floor', RoomObject.floor)
            RoomObject.availability = data.get('availability', RoomObject.availability)
            RoomObject.image = data.get('image', RoomObject.image)
        except Room.DoesNotExists:
            return None
        

    RoomObject.save()

    return RoomObject

def getAppointments(showResolved = False):
    return Appointment.objects.filter(resolved = showResolved).order_by('-timeStamp')

def addAppointmentRecord(data:dict):
    AppointmentObject = Appointment(
        name = data.get('name'),
        email = data.get('email'),
        topic = data.get('topic'),
        message = data.get('message'),
        ipAddress = data.get('ipAddress'))
    AppointmentObject.save()

def deleteAppointmentRecord(id:int):
    Appointment.objects.filter(id = id).delete()

def deleteRoomRecord(id:int):
    Room.objects.filter(id = id).delete()

def wipeAppointmentRecords():
    Appointment.objects.all().delete()
    
def resolveAppointmentRecord(id:int):
    temp = Appointment.objects.get(id = id)
    temp.resolved = True
    temp.save()

def getRoomImage(id:int):
    temp = Room.objects.get(id = id)
    return temp.image

def register(data:dict, picture):
    username = data.get('username')
    first_name = data.get('firstname')
    last_name = data.get('lastname')
    email = data.get('email')
    password = data.get('password')
    avatar = picture
    user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
    group = Group.objects.get(name='User')
    user.groups.add(group)
    profile = UserProfile(user=user, avatar=avatar)
    profile.save()

def getUserPicture(userID:int):
    try:
        userPicture = UserProfile.objects.get(user = userID).avatar
        return userPicture
    except:
        return None
    
def getReviews(roomID:int):
    reviewList = Review.objects.filter(roomID = roomID)
    return reviewList

def getReviewAverageScores(roomID:int):
    return Review.objects.filter(roomID = roomID).aggregate(Avg('cleanlinessRating'), Avg('aestheticRating'), Avg('comfortRating'), Avg('valueRating'))
    
def postReview():
    pass

def addSuggestionRecord(data:dict):
    SuggestionObject = Suggestion(
        topic = data.get('topic'),
        message = data.get('message', ''),
        userID = data.get('userID'))
    SuggestionObject.save()

def getSuggestions(showResolved = False, showFavourite = False):    
    return Suggestion.objects.filter(favourite = showFavourite).filter(resolved = showResolved).order_by('-timeStamp')

def toggleResolvedSuggestion(id:int):
    temp = Suggestion.objects.get(id = id)
    temp.resolved = not temp.resolved
    temp.save()

def toggleFavouriteSuggestion(id:int):
    temp = Suggestion.objects.get(id = id)
    temp.favourite = not temp.favourite
    temp.save()