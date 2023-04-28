from random import choice
import random

import usaddress
from django.db import models
from django.db.models.constraints import UniqueConstraint
from django.contrib.auth.models import User

from faker import Faker

fake = Faker()


class Users(User):
    RENTER = 'renter'
    AGENT = 'agent'
    USER_TYPE = [
        (RENTER, 'Renter'),
        (AGENT, 'Agent')
    ]
    user_type = models.TextField(choices=USER_TYPE, default=RENTER)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    """
    To use Faker to generate fake data, run the following command in the terminal:
    
    > python manage.py shell
    > from dj_backend.models import Users
    > Users.generate_fake_data(10)
    """

    @classmethod
    def generate_fake_data(cls, n):
        for i in range(n):
            user_profile = cls(
                user_email=fake.email(),
                user_last_name=fake.last_name(),
                user_first_name=fake.first_name(),
                user_type=fake.random_element(elements=('renter', 'agent')),
                user_password=fake.password(),
            )
            user_profile.save()


class Renters(Users):
    rental_preferences = models.CharField(max_length=100)
    desired_move_in_date = models.DateField()
    preferred_location = models.CharField(max_length=100)
    budget = models.FloatField()
    total_cost = models.DecimalField(max_digits=20, decimal_places=2)

    @classmethod
    def generate_fake_data(cls, n):
        for i in range(n):
            renter_profile = cls(
                user_email=fake.email(),
                user_last_name=fake.last_name(),
                user_first_name=fake.first_name(),
                user_type=fake.random_element(elements=('renter', 'agent')),
                user_password=fake.password(),
                rental_preferences=fake.text(),
                desired_move_in_date=fake.date(),
                preferred_location=fake.address(),
                budget=fake.random_int(min=0, max=1000000),
                total_cost=fake.random_int(min=0, max=1000000)
            )
            renter_profile.save()


class Property(models.Model):
    property_id = models.AutoField(primary_key=True)
    property_type = models.CharField(max_length=20)
    property_description = models.CharField(max_length=100)
    property_city = models.CharField(max_length=20)
    property_state = models.CharField(max_length=20)
    property_address = models.CharField(max_length=100)
    property_price = models.FloatField()
    property_availability = models.BooleanField(default="True")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, to_field='id')


#     Randomly generate Property
#     python manage.py shell
#     from dj_backend.models import Property
#     Property.generate_random_subclass_data(10)

    # delete：Property.delete_fake_data()



    @classmethod
    def generate_random_subclass_data(cls, n):
        subclasses = cls.__subclasses__()
        for _ in range(n):
            subclass = random.choice(subclasses)
            subclass.generate_fake_data(1)

    @classmethod
    def generate_fake_data(cls, n, property_type, extra_fields=None):
        extra_fields = extra_fields or {}
        for _ in range(n):
            user = choice(User.objects.all())
            full_address = fake.address()
            parsed_address = usaddress.parse(full_address)
            address_dict = {k: v for (v, k) in parsed_address}

            city = address_dict.get('PlaceName', '')
            state = address_dict.get('StateName', '')
            property_data = {
                'property_type': property_type,
                'property_description': fake.text(),
                'property_city': city,
                'property_state': state,
                'property_address': fake.address(),
                'property_price': fake.random_int(min=100, max=10000),
                'property_availability': fake.boolean(),
                'user_id': user,
                **extra_fields
            }
            instance = cls(**property_data)
            instance.save()

    @classmethod
    def delete_fake_data(cls):
        subclasses = cls.__subclasses__()
        for subclass in subclasses:
            subclass.objects.all().delete()
        cls.objects.all().delete()

class CreditCard(models.Model):
    credit_card_id = models.AutoField(primary_key=True)
    number = models.CharField(max_length=20)
    holder_name = models.CharField(max_length=20)
    expiry_date = models.DateField()
    cvv = models.IntegerField()
    street = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    zip = models.IntegerField()
    country = models.CharField(max_length=20)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, to_field='id')


class Booking(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, to_field='id')
    property_id = models.ForeignKey(Property, on_delete=models.CASCADE, to_field='property_id')
    credit_card_id = models.ForeignKey(CreditCard, on_delete=models.CASCADE, to_field='credit_card_id')

    start_date = models.DateField()
    end_date = models.DateField()
    total_cost = models.DecimalField(max_digits=20, decimal_places=2)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['user_id', 'property_id', 'credit_card_id'], name='unique_booking')
        ]


class UserAddress(models.Model):
    user_address_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, to_field='id')

    street = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zip = models.IntegerField()
    country = models.CharField(max_length=20)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['user_address_id', 'user_id'], name='unique_user_address')
        ]


class RewardRecord(models.Model):
    reward_record_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, to_field='id')
    property_id = models.ForeignKey(Property, on_delete=models.CASCADE, to_field='property_id')


class Agents(Users):
    job_title = models.CharField(max_length=20)
    company = models.CharField(max_length=20)
    contact_information = models.CharField(max_length=20)


class Neighborhood(models.Model):
    neighborhood_id = models.AutoField(primary_key=True)
    property_id = models.ForeignKey(Property, on_delete=models.CASCADE, to_field='property_id')
    crime_rate = models.FloatField()
    nearby_schools = models.CharField(max_length=100)


class House(Property):
    num_of_rooms = models.IntegerField()

    @classmethod
    def generate_fake_data(cls, n):
        extra_fields = {'num_of_rooms': fake.random_int(min=1, max=3)}
        super().generate_fake_data(n, 'House', extra_fields)


class Apartment(Property):
    num_of_rooms = models.IntegerField()
    building_type = models.CharField(max_length=20)

    @classmethod
    def generate_fake_data(cls, n):
        extra_fields = {
            'num_of_rooms': fake.random_int(min=1, max=3),
            'building_type': fake.random_element(elements=('Condominium', 'Loft', 'Duplex'))
        }
        super().generate_fake_data(n, 'Apartment', extra_fields)


class CommercialBuilding(Property):
    business_type = models.CharField(max_length=20)

    @classmethod
    def generate_fake_data(cls, n):
        extra_fields = {'business_type': fake.random_element(elements=('Retail', 'Office', 'Industrial', 'Mixed Use'))}
        super().generate_fake_data(n, 'CommercialBuilding', extra_fields)


class Land(Property):
    land_size = models.FloatField()

    @classmethod
    def generate_fake_data(cls, n):
        extra_fields = {'land_size': round(random.uniform(0.1, 1000), 2)}
        super().generate_fake_data(n, 'Land', extra_fields)


class VacationHome(Property):
    characteristics = models.CharField(max_length=20)

    @classmethod
    def generate_fake_data(cls, n):
        extra_fields = {'characteristics': fake.random_element(elements=('Beachfront', 'Mountain', 'Lake', 'Urban'))}
        super().generate_fake_data(n, 'Vacation Home', extra_fields)
