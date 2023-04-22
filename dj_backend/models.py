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
    total_cost = models.DecimalField(max_digits=20, decimal_places=2)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    about_me = models.TextField(blank=True, null=True)
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
                total_cost=fake.random_int(min=0, max=1000000)
            )
            user_profile.save()


class Renters(models.Model):
    # use to_filed to specify the foreign key to the primary key (user_id) of the user profile
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, to_field='id', primary_key=True)
    renter_rental_preferences = models.CharField(max_length=100)
    renter_desired_move_in_date = models.DateField()
    renter_preferred_location = models.CharField(max_length=100)
    renter_budget = models.FloatField()


class Property(models.Model):
    property_id = models.AutoField(primary_key=True)
    property_type = models.CharField(max_length=20)
    property_description = models.CharField(max_length=100)
    property_city = models.CharField(max_length=20)
    property_state = models.CharField(max_length=20)
    property_address = models.CharField(max_length=100)
    property_price = models.FloatField()
    property_availability = models.BooleanField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, to_field='id')


class CreditCard(models.Model):
    credit_card_id = models.AutoField(primary_key=True)
    credit_card_number = models.CharField(max_length=20)
    credit_card_holder_name = models.CharField(max_length=20)
    credit_card_expiry_date = models.DateField()
    credit_card_cvv = models.IntegerField()
    credit_card_street = models.CharField(max_length=20)
    credit_card_city = models.CharField(max_length=20)
    credit_card_zip = models.IntegerField()
    credit_card_country = models.CharField(max_length=20)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, to_field='id')


class Booking(models.Model):
    user_id = models.ForeignKey(Renters, on_delete=models.CASCADE, to_field='user_id')
    property_id = models.ForeignKey(Property, on_delete=models.CASCADE, to_field='property_id')
    credit_card_id = models.ForeignKey(CreditCard, on_delete=models.CASCADE, to_field='credit_card_id')

    booking_start_date = models.DateField()
    booking_end_date = models.DateField()
    booking_total_cost = models.DecimalField(max_digits=20, decimal_places=2)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['user_id', 'property_id', 'credit_card_id'], name='unique_booking')
        ]


class UserAddress(models.Model):
    user_address_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, to_field='id')

    user_address_street = models.CharField(max_length=20)
    user_address_city = models.CharField(max_length=20)
    user_address_state = models.CharField(max_length=20)
    user_address_zip = models.IntegerField()
    user_address_country = models.CharField(max_length=20)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['user_address_id', 'user_id'], name='unique_user_address')
        ]


class RewardRecord(models.Model):
    reward_record_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, to_field='id')
    property_id = models.ForeignKey(Property, on_delete=models.CASCADE, to_field='property_id')


class Agents(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, to_field='id', primary_key=True)
    agent_job_title = models.CharField(max_length=20)
    agent_company = models.CharField(max_length=20)
    agent_contact_information = models.CharField(max_length=20)


class Neighborhood(models.Model):
    neighborhood_id = models.AutoField(primary_key=True)
    property_id = models.ForeignKey(Property, on_delete=models.CASCADE, to_field='property_id')
    crime_rate = models.FloatField()
    nearby_schools = models.CharField(max_length=100)


class House(models.Model):
    property_id = models.OneToOneField(Property, on_delete=models.CASCADE, to_field='property_id', primary_key=True)
    num_of_rooms = models.IntegerField()


class Apartment(models.Model):
    property_id = models.OneToOneField(Property, on_delete=models.CASCADE, to_field='property_id', primary_key=True)
    num_of_rooms = models.IntegerField()
    building_type = models.CharField(max_length=20)


class CommercialBuilding(models.Model):
    property_id = models.OneToOneField(Property, on_delete=models.CASCADE, to_field='property_id', primary_key=True)
    business_type = models.CharField(max_length=20)


class Land(models.Model):
    property_id = models.OneToOneField(Property, on_delete=models.CASCADE, to_field='property_id', primary_key=True)
    land_size = models.FloatField()


class VacationHome(models.Model):
    property_id = models.OneToOneField(Property, on_delete=models.CASCADE, to_field='property_id', primary_key=True)
    characteristics = models.CharField(max_length=20)
