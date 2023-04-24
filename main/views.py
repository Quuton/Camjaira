from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib import auth
from .modelInterface import *
from .utility import *

mainPath = 'main/'


def test(request):
    # The test function is used to test any new feature i add
    # It makes it easier since i have one dedicated test page
    
    context = {
        'recent': getRecentPosts(),
        'suggestion':getSuggestions()
    }

    return render(request, mainPath + 'test.html/', context=context)

def suggestionList(request):
    context = {
        'recent': getRecentPosts(),
        'suggestion':getSuggestions()
    }
    return render(request, mainPath + 'suggestionList.html/', context=context)

def roomList(request):
    queryData = None

    priceMin = parseFloat(request.GET.get('priceMin', '0'))
    priceMax = parseFloat(request.GET.get('priceMax', '0'))


    if request.method == 'GET':
        queryData = {
            'query': request.GET.get('query', ''),
            'queryType': request.GET.get('queryType', 'type'),
            'priceMin': priceMin,
            'priceMax': priceMax,
            'orderField': request.GET.get('orderField', 'id'),
            'orderDirection': (request.GET.get('orderDirection', 'ascending') == 'ascending'),
        }

        context = {
            'recent': getRecentPosts(),
            'rooms': getRooms(queryData),
        }

    return render(request, mainPath + 'roomTable.html', context=context)


def services(request):

    context = {
        'recent': getRecentPosts(),
        'rooms': getFeaturedRooms(100),
    }

    return render(request, mainPath + 'services.html', context=context)

def forbidden(request):
    return render(request, mainPath + 'forbidden.html', context=None)

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
    if isUser(request):
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

        else:
            context = {
                'recent': getRecentPosts(),
                'appointmentSaveStatus': status,
            }
            
        return render(request, mainPath + 'contact.html', context=context)
    else:
        return redirect('/login')



def about(request):

    context = {
        'recent': getRecentPosts(),
    }

    return render(request, mainPath + 'about.html', context=context)


def appointments(request):
    if request.method == 'GET' and isOwner(request):
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
        return redirect('/forbidden')


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


def roomEdit(request, id: int):
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

def roomCreate(request):
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
        return render(request, mainPath + 'roomCreate.html', context=context)
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
        'averages':getReviewAverageScores(id),
    }

    return render(request, mainPath + 'roomDetail.html', context=context)

def registerUser(request):
    context = {
        'recent': getRecentPosts(),
    }

    if request.method == 'POST':
        register(request.POST, request.FILES['avatar'])
        return redirect('/')
    else:
        return render(request, mainPath + 'registerUser.html', context=context)

def userPage(request):
    userGroup = None
    if request.user.groups.all():
        userGroup = request.user.groups.all()[0]
    else:
        return redirect('/login')

    context = {
        'recent': getRecentPosts(),
        'accountType': userGroup,
        'superUser': request.user.is_superuser,
        'picture': getUserPicture(request.user.id),
        'userid': request.user.id,
        'username':request.user.username,
        'isUser': isUser(request),
        'isAdmin': isAdmin(request),
        'isOwner': isOwner(request),
    }
    return render(request, mainPath + 'userPage.html/', context=context)

def roomListReview(request, id: int):

    context = {'recent':getRecentPosts(),
                'reviewList':getReviews(id)}

    return render(request, mainPath + 'roomListReview.html/', context=context)
