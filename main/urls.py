
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test),
    path('services/', views.services),
    path('login/', views.login),
    path('logout/', views.logout),
    path('contact/', views.contact),
    path('about/', views.about),
    path('delete-appointment/<int:id>', views.deleteAppointment),
    path('appointments/', views.appointments),
    path('wipe-appointments/', views.wipeAppointments),
    path('resolve-appointment/<int:id>', views.resolveAppointment),
    path('delete-room/<int:id>', views.deleteRoom),
    path('show-room/<int:id>', views.roomDetail),
    path('edit-room/<int:id>', views.roomEdit),
    path('create-room/', views.roomCreate),
    path('list-room/', views.roomList),
    path('register', views.registerUser),
    path('user', views.userPage),
    path('', views.home),
]
