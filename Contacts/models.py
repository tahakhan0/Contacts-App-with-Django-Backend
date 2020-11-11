from django.db import models
from django.core.validators import MinValueValidator


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(null=True, blank=True, max_length=50)
    company = models.CharField(null=True, blank=True, max_length=50)
    notes = models.TextField(null=True, blank=True, max_length=140)

    class Meta:
        verbose_name_plural = "Contacts"

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class PhoneNumbers(models.Model):
    number = models.CharField(null=True, blank=True, max_length=15)
    contact = models.ForeignKey(
        Contact, on_delete=models.CASCADE, blank=True,
        null=True, related_name='phone')

    class Meta:
        verbose_name_plural = "Phone Numbers"

    def __str__(self):
        return self.number


class Email(models.Model):
    email = models.EmailField(null=True, blank=True, max_length=254)
    contact = models.ForeignKey(
        Contact, on_delete=models.CASCADE, blank=True,
        null=True, related_name='email')

    class Meta:
        verbose_name_plural = "Email ids"

    def __str__(self):
        return self.email


class Address(models.Model):
    street = models.CharField(null=True, blank=True, max_length=120)
    street_detail = models.CharField(null=True, blank=True, max_length=50)
    city = models.CharField(null=True, blank=True, max_length=50)
    zipcode = models.CharField(
        null=True, blank=True, max_length=8)
    country = models.CharField(null=True, blank=True, max_length=50)
    contact = models.ForeignKey(
        Contact, on_delete=models.CASCADE, blank=True,
        null=True, related_name='address')

    class Meta:
        verbose_name_plural = "Addresses"

    def __str__(self):
        return '{} {} {} {}'.format(self.street, self.street_detail, self.city, self.country)


class SocialMedia(models.Model):
    url = models.CharField(null=True, blank=True, max_length=250)
    contact = models.ForeignKey(
        Contact, on_delete=models.CASCADE, blank=True,
        null=True, related_name='social_media')

    class Meta:
        verbose_name_plural = "Social Media profiles"
