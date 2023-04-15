from django.db import models
from faker import Faker

fake = Faker()


class UserProfile(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=50)

    @classmethod
    def generate_fake_data(cls, n):
        for i in range(n):
            user_profile = cls(
                email=fake.email(),
                password=fake.password(),
            )
            user_profile.save()
