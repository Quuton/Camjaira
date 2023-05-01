
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('test/', views.test),
    path('about/', views.about),
    path('login/', views.login),
    path('user/', views.userPage),
    path('logout/', views.logout),
    path('contact/', views.contact),
    path('services/', views.services),
    path('list-room/', views.roomList),
    path('forbidden/', views.forbidden),
    path('register/', views.registerUser),
    path('create-room/', views.roomCreate),
    path('appointments/', views.appointments),
    path('edit-room/<int:id>', views.roomEdit),
    path('show-room/<int:id>', views.roomDetail),
    path('delete-room/<int:id>', views.deleteRoom),
    path('suggestion-list/', views.suggestionList),
    path('suggestion-create/', views.suggestionCreate),
    path('resolve-suggestion/<int:id>',views.resolveSuggestion),
    path('wipe-appointments/', views.wipeAppointments),
    path('favourite-suggestion/<int:id>',views.favouriteSuggestion),
    path('show-reviews-room/<int:id>', views.roomListReview),
    path('add-review/<int:roomID>', views.addReview),
    path('delete-appointment/<int:id>', views.deleteAppointment),
    path('resolve-appointment/<int:id>', views.resolveAppointment),
]
