from django.db import models
from django.contrib.auth.models import User


class PilotPost(models.Model):
    """ Docstring """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', default='../default_post_y8afhe')


    class Meta:
        """ Docstring """
        ordering = ['-updated_at']
    

    def __str__(self):
        return f'Pilot post: {self.id}'