from .models import *
import math
import itertools as it

def testFunction(n:int):
    for i in range(0,n):
        newRoomObj = Room(number = 'testobj' + str(i), description = 'Test description', floor = i, image = 'room_images/Draco.png', size = 200, price = 69420, availability = True, type = 'Single')
        newRoomObj.save()
    for i in range(0,n):
        newRoomObj = Room(number = 'testobj' + str(i), description = 'Test description', floor = i, image = 'room_images/Draco.png', size = 200, price = 69420, availability = True, type = 'Studio')
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
    
    print(f'query process part 1: {querySet}')

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
    
    print(f'query process part 2: {querySet}')

    querySet = querySet.filter(price__gte = queryData['priceMin'])

    print(f'query process part 3: {querySet}')

    if queryData['priceMax'] != 0:
        querySet = querySet.filter(price__lte = queryData['priceMax'])
        
    print(f'query process part 4: {querySet}')
    return querySet

        

def getRoom(id:int):
    temp = Room.objects.get(id = id)
    temp.visitCount += 1
    temp.save()
    
    return Room.objects.get(id = id)

def getAppointments(showResolved = False):
    if showResolved :
        return Appointment.objects.all().order_by('-timeStamp')
    else:
        return Appointment.objects.filter(resolved = False).order_by('-timeStamp')

def addAppointmentRecord(data:dict):
    AppointmentObject = Appointment(
        name = data['name'],
        email = data['email'],
        topic = data['topic'],
        message = data['message'],
        ipAddress = data['ipAddress'])
    AppointmentObject.save()

def saveRoomRecord(data:dict, id:int = None):
    if id == None:
        RoomObject = Room ( 
            number = data['number'],
            description = data['description'],
            price = data['price'],
            size = data['size'],
            type = data['type'],
            floor = data['floor'],
            availability = data['availability'],
            image = data['image'])
    else:
        RoomObject = Room.objects.get(id = id)
        RoomObject.number = data['number']
        RoomObject.description = data['description']
        RoomObject.price = data['price']
        RoomObject.size = data['size']
        RoomObject.type = data['type']
        RoomObject.floor = data['floor']
        RoomObject.availability = data['availability']
        RoomObject.image = data['image']

    RoomObject.save()

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
