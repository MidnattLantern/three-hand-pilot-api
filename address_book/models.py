from django.db import models
from django.contrib.auth.models import User


class Address(models.Model):
    """ Docstring """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    partnering_end = models.CharField(max_length=50)


    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return f'{self.id} {self.partnering_end}'