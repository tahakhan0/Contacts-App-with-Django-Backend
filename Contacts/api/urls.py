from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('contacts/add', CreateContactsView.as_view()),
    path('contacts/<pk>', RetrieveUpdateDestroyContactsView.as_view()),
    path("contacts/", ContactsView.as_view()),
    path('phone/', PhoneNumbersView.as_view()),
    path('emails/', EmailView.as_view())
]
