from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver




class Profile(models.Model):
    # one to one relationship between user and profile
    user = models.OneToOneField(User,on_delete= models.CASCADE)
    #city
    city = models.ForeignKey('City',related_name='user_city', on_delete= models.CASCADE, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    image = models.ImageField(upload_to='profile/', blank=True, null=True)

    def __str__(self):
        return str(self.user)

## create new user ---> create new profile

@receiver(post_save, sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
    
    


class City(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return str(self.name)

