import time


from django.contrib.auth.models import AbstractUser
from django.db import models
from .photo_conv import watermark_with_transparency
from rest.settings import BASE_DIR, MEDIA_ROOT

class User(AbstractUser):
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    GENDERS = (
        ('male', 'MALE'),
        ('female', 'FEMALE'),
    )
    gender = models.CharField(max_length=10, choices=GENDERS)

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     # super(User, self).save(*args, **kwargs)
    #     tmp_path = MEDIA_ROOT / self.photo.path
    #     watermark_with_transparency(tmp_path)
    #     print(tmp_path)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        tmp_path = MEDIA_ROOT / self.photo.path
        watermark_with_transparency(tmp_path)
        print(tmp_path)
        # super(User, self).save(*args, **kwargs)



class Like(models.Model):
   owner = models.ForeignKey(User, related_name="like_owner", on_delete=models.CASCADE)
   likee = models.ForeignKey(User, related_name="like_likee", on_delete=models.CASCADE)

   def __str__(self):
       return f'{self.owner} -> {self.likee}'
