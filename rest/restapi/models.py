from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='users', on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    GENDERS = (
        ('male', 'MALE'),
        ('female', 'FEMALE'),
    )
    gender = models.CharField(max_length=300, choices=GENDERS)

    def __str__(self):
        return f'Profile for user {self.user.username}'



class Like(models.Model):
   owner = models.ForeignKey(User, related_name="like_owner", on_delete=models.CASCADE)
   likee = models.ForeignKey(User, related_name="like_likee", on_delete=models.CASCADE)

   def __str__(self):
       return f'{self.owner} -> {self.likee}'
