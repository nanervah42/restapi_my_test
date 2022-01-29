

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    GENDERS = (
        ('male', 'MALE'),
        ('female', 'FEMALE'),
    )
    gender = models.CharField(max_length=10, choices=GENDERS)


class Like(models.Model):
   owner = models.ForeignKey(User, related_name="like_owner", on_delete=models.CASCADE)
   likee = models.ForeignKey(User, related_name="like_likee", on_delete=models.CASCADE)

   def __str__(self):
       return f'{self.owner} -> {self.likee}'
