import imp
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


# when User is saved send signal 'post_save'(instance of User, created) to a receiver/create_profiles()
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, *args, **kwargs):
    # if User was created the create Profile object with user = instance
    if created:
      Profile.objects.create(user=instance)


# save profile when the User is saved
@receiver(post_save, sender=User)
def save_profile(sender, instance, *args, **kwargs):
    instance.profile.save()