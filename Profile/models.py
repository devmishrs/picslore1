from django.db import models
from django.db.models.signals import post_save
from django.utils import timezone
from django.db.models import Q

from accounts.models import User

class UserProfile(models.Model):
    profile_pic = models.ImageField(blank= True)
    user_prof = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField('Address', max_length= 1000, blank= True)
    city = models.CharField('City', max_length = 33, blank= True)
    state = models.CharField('State', max_length = 33, blank= True)
    country = models.CharField('Country', max_length = 33, blank= True)

    def __str__(self):
        return self.user_prof.username

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user_prof = kwargs['instance'])

post_save.connect(create_profile, sender = User)







