from django.contrib import admin
from Contacts.models import *


# Important Link https://youtu.be/e73TvQlqzzc

class PhoneNumbersInline(admin.TabularInline):
    model = PhoneNumbers
    extra = 1


class AdressInline(admin.StackedInline):
    model = Address
    extra = 1


class EmailInline(admin.TabularInline):
    model = Email
    extra = 1


class SocialMediaInline(admin.TabularInline):
    model = SocialMedia
    extra = 1


# @admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    inlines = [
        PhoneNumbersInline,
        AdressInline,
        EmailInline,
        SocialMediaInline
    ]

    class Meta:
        model = Contact


admin.site.register(Contact, ContactAdmin)
admin.site.register(PhoneNumbers)
admin.site.register(Email)
admin.site.register(SocialMedia)
# admin.site.register(Contact)
admin.site.register(Address)
