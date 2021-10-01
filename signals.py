from . models import profile

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def post_save_create_profile(sender, instance, created, **kwargs):
    if created:
        profile.objects.create(user=instance)
        print(f'{sender} - {instance} - {created}')




#using django signels - will take in data from user and runs function


#User to profile