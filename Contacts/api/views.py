from .serializers import *
from rest_framework import generics
from Contacts.models import *


class ContactsView(generics.ListAPIView):
    queryset = Contact.objects.all().order_by('first_name')
    serializer_class = ContactSerializer


class CreateContactsView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = CreateContactSerializer


class RetrieveUpdateDestroyContactsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = CreateContactSerializer


class PhoneNumbersView(generics.ListAPIView):
    queryset = PhoneNumbers.objects.all()
    serializer_class = PhoneNumberSerializer


class EmailView(generics.ListAPIView):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer
