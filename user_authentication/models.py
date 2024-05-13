from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class UserAuthentication(models.Model):
    """ Id is automatic """
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_rmkaor'
    )

    class Meta:
        """ Meta class for User Authentication """
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Authentication for {self.owner}"


def create_user_authentication(sender, instance, created, **kwargs):
    if created:
        UserAuthentication.objects.create(owner=instance)

post_save.connect(create_user_authentication, sender=User)
