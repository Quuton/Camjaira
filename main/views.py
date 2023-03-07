from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib import auth
from .utility import *

mainPath = 'main/'
# ALL CODE BELOW IS STILL FOR TESTING, NO FINAL COMMITMENT


def test(request):
    context = {
        'recent': getRecentPosts(),
    }

    testFunction(10)

    return render(request, mainPath + 'test.html/', context=context)


def listRoom(request):
    data = None

    # Prevent empty strings so we can convert to float
    if request.GET.get('priceMin', '0') != '' and request.GET.get('priceMin', '0').isnumeric():
        priceMin = float(request.GET.get('priceMin', '0'))
    else:
        priceMin = 0.0

    if request.GET.get('priceMax', '0') != '' and request.GET.get('priceMax', '0').isnumeric():
        priceMax = float(request.GET.get('priceMax', '0'))
    else:
        priceMax = 0.0

    if request.method == 'GET':
        data = {
            'query': request.GET.get('query', ''),
            'queryType': request.GET.get('queryType', 'type'),
            'priceMin': priceMin,
            'priceMax': priceMax,
            'orderField': request.GET.get('orderField', 'id'),
            'orderDirection': (request.GET.get('orderDirection', 'ascending') == 'ascending'),
        }

        context = {
            'recent': getRecentPosts(),
            'rooms': getRooms(data),
        }

    print(f'data is {data}')
    return render(request, mainPath + 'roomTable.html', context=context)


def services(request):

    context = {
        'recent': getRecentPosts(),
        'rooms': getFeaturedRooms(100),
    }

    return render(request, mainPath + 'services.html', context=context)


def home(request):
    context = {
        'recent': getRecentPosts(),
        'rooms': getFeaturedRooms()
    }

    return render(request, mainPath + 'index.html', context=context)


def login(request):

    context = {
        'recent': getRecentPosts(),
    }

    return render(request, mainPath + 'login.html', context=context)


def contact(request):
    status = False
    if request.method == "POST":
        data = {
            "name": request.POST['name'],
            "email": request.POST['email'],
            "topic": request.POST['topic'],
            "message": request.POST['message'],
            "ipAddress": request.META.get("REMOTE_ADDR"),
        }
        addAppointmentRecord(data)
        status = True

    context = {
        'recent': getRecentPosts(),
        'appointmentSaveStatus': status,
    }

    return render(request, mainPath + 'contact.html', context=context)


def about(request):

    context = {
        'recent': getRecentPosts(),
    }

    return render(request, mainPath + 'about.html', context=context)


def appointments(request):
    if request.method == 'GET' and request.user.is_authenticated:
        print(request.GET.get('showResolved', 'off'))
        if request.GET.get('showResolved', 'off') == 'on':
            context = {
                'recent': getRecentPosts(),
                'rooms': getFeaturedRooms(),
                'appointments': getAppointments(True),
                'appointmentParams': request.GET,
            }
        else:
            context = {
                'recent': getRecentPosts(),
                'rooms': getFeaturedRooms(),
                'appointments': getAppointments(False),
                'appointmentParams': request.GET,
            }
        return render(request, mainPath + 'appointments.html', context=context)
    else:
        return render(request, mainPath + 'forbidden.html', context=None)


def deleteAppointment(request, id: int):
    deleteAppointmentRecord(id)
    return redirect('/appointments')


def wipeAppointments(request):
    wipeAppointmentRecords()
    return redirect('/appointments')


def resolveAppointment(request, id: int):
    resolveAppointmentRecord(id)
    return redirect('/appointments')


def deleteRoom(request, id: int):
    deleteRoomRecord(id)
    return redirect('/services')


def editRoom(request, id: int):
    status = False
    if request.method == "POST" and request.user.is_authenticated:
        data = {
            "number": request.POST['number'],
            "description": request.POST['description'],
            "availability": (request.POST.getlist('availability') != []),
            "type": request.POST['type'],
            "floor": request.POST['floor'],
            "price": request.POST['price'],
            "size": request.POST['size'],
            'image': request.FILES.get('image')
        }
        roomID = request.POST['roomID']
        print(data['image'])
        # If no image selected, lets the record keep the old one.
        if request.FILES.get('image') == None:
            data['image'] = getRoomImage(roomID)


        saveRoomRecord(data=data, id=roomID)
        status = True

    context = {
        'recent': getRecentPosts(),
        'room': getRoom(id),
        'roomSaveStatus': status,
    }

    if request.user.is_authenticated:
        return render(request, mainPath + 'roomEdit.html', context=context)
    else:
        return render(request, mainPath + 'forbidden.html', context=None)

def createRoom(request):
    context = {
        'recent': getRecentPosts(),
    }
    if request.method == "POST" and request.user.is_authenticated:
        data = {
            "number": request.POST['number'],
            "description": request.POST['description'],
            "availability": (request.POST.getlist('availability') != []),
            "type": request.POST['type'],
            "floor": request.POST['floor'],
            "price": request.POST['price'],
            "size": request.POST['size'],
            'image': request.FILES.get('image')
        }
        saveRoomRecord(data = data)
        return redirect('/services/')

    if request.user.is_authenticated:
        return render(request, mainPath + 'createRoom.html', context=context)
    else:
        return render(request, mainPath + 'forbidden.html', context=None)


def login(request):
    context = {
        'recent': getRecentPosts(),
        'loginStatus': ''
    }

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            context['loginStatus'] = 'Username or Password does not match with an account'

    return render(request, mainPath + 'login.html', context=context)


def logout(request):
    auth.logout(request)
    return redirect('/')


def roomDetail(request, id: int):
    context = {
        'recent': getRecentPosts(),
        'room': getRoom(id),
    }

    return render(request, mainPath + 'roomDetail.html', context=context)
