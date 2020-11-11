from rest_framework import serializers

from Contacts.models import *


class PhoneNumberSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = PhoneNumbers
        fields = "__all__"

        read_only_fields = ('contact',)


class PhoneNumberSerializerForContact(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumbers
        fields = ['number', 'contact']


class AddressSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Address
        fields = "__all__"

        read_only_fields = ('contact',)


class EmailSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Email
        fields = "__all__"

        read_only_fields = ('contact',)


class SocialMediaSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = SocialMedia
        fields = "__all__"
        read_only_fields = ('contact',)


class ContactSerializer(serializers.ModelSerializer):
    phone = serializers.SerializerMethodField()
    address = serializers.SerializerMethodField()
    social_media = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()

    class Meta:
        model = Contact
        fields = ["id", "first_name", "last_name", "company",
                  "notes", "phone", "address", "social_media", "email"]
    '''
    Note the use of contact_phone below. It is the related_name set for foreign key in PhoneNumbers' Model
    '''

    def get_phone(self, obj):
        return [PhoneNumberSerializerForContact(s).data for s in obj.phone.all()]

    def get_address(self, obj):
        return [AddressSerializer(s).data for s in obj.address.all()]

    def get_social_media(self, obj):
        return [SocialMediaSerializer(s).data for s in obj.social_media.all()]

    def get_email(self, obj):
        return [EmailSerializer(s).data for s in obj.email.all()]


class CreateContactSerializer(serializers.ModelSerializer):
    phone = PhoneNumberSerializer(many=True, allow_null=True)
    address = AddressSerializer(many=True, allow_null=True)
    social_media = SocialMediaSerializer(many=True, allow_null=True)
    email = EmailSerializer(many=True, allow_null=True)

    class Meta:
        model = Contact
        fields = ["pk", "first_name", "last_name", "company",
                  "notes", "phone", "email", "address", 'social_media']

    def create(self, validated_data):
        phone = validated_data.pop('phone')
        email = validated_data.pop('email')
        address = validated_data.pop('address')
        social = validated_data.pop('social_media')

        contact = Contact.objects.create(**validated_data)

        if phone:
            for nums in phone:
                PhoneNumbers.objects.create(**nums, contact=contact)
        if email:
            for e in email:
                Email.objects.create(**e, contact=contact)

        if address:
            for a in address:
                Address.objects.create(**a, contact=contact)

        if social:
            for s in social:
                SocialMedia.objects.create(**s, contact=contact)

        return contact

    def update(self, instance, validated_data):
        email = validated_data.pop('email')
        address = validated_data.pop('address')
        social_media = validated_data.pop('social_media')
        phone = validated_data.pop('phone')

        instance.first_name = validated_data.get(
            "first_name", instance.first_name)
        instance.last_name = validated_data.get(
            "last_name", instance.last_name)
        instance.notes = validated_data.get("notes", instance.notes)
        instance.save()

        keep_email = []
        keep_address = []
        keep_social_media = []
        keep_phone = []

        def func(name, instance_obj, local_attribute, keep_type, model):
            for e in name:
                if "id" in e.keys():
                    if model.objects.filter(id=e["id"]).exists():
                        c = model.objects.get(id=e["id"])

                        if local_attribute == "url":
                            c.url = e.get(local_attribute, c.url)
                        elif local_attribute == "email":
                            c.email = e.get(local_attribute, c.email)
                        elif local_attribute == "number":
                            c.number = e.get(local_attribute, c.number)
                        else:
                            c.street = e.get("street", c.street)
                            c.street_detail = e.get(
                                'street_detail', c.street_detail)
                            c.city = e.get("city", c.city)
                            c.zipcode = e.get("zipcode", c.zipcode)
                            c.country = e.get("country", c.country)
                        c.save()
                        keep_type.append(c.id)
                    else:
                        continue
                else:
                    c = model.objects.create(**e, contact=instance)
                    keep_type.append(c.id)

            for name in instance_obj:
                if name.id not in keep_type:
                    name.delete()

        update_social_media = func(name=social_media, instance_obj=instance.social_media.all(
        ), local_attribute='url', keep_type=keep_social_media, model=SocialMedia)

        update_email = func(name=email, instance_obj=instance.email.all(
        ), local_attribute='email', keep_type=keep_email, model=Email)

        update_phone = func(name=phone, instance_obj=instance.phone.all(
        ), local_attribute='number', keep_type=keep_phone, model=PhoneNumbers)

        update_address = func(name=address, instance_obj=instance.address.all(
        ), local_attribute=None, keep_type=keep_address, model=Address)

        return instance


"""
for e in email:
            print(e.keys())
            if "id" in e.keys():
                if Email.objects.filter(id=e["id"]).exists():
                    c = Email.objects.get(id=e["id"])
                    c.text = e.get('email', c.email)
                    c.save()
                    keep_email.append(c.id)
                else:
                    continue
            else:
                c = Email.objects.create(**e, contact=instance)
                keep_email.append(c.id)

        for email in instance.email.all():
            if email.id not in keep_email:
                email.delete()
"""
