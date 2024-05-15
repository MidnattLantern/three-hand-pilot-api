from django.db import models
from django.contrib.auth.models import User


class Address(models.Model):
    """ Docstring """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    partnering_end = models.CharField(max_length=50)
    address_line1 = models.CharField(max_length=255, blank=True, null=True)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    contact_person_name = models.CharField(max_length=255, blank=True, null=True)
    contact_phone_number = models.CharField(max_length=20, blank=True, null=True)
#    contact_email = models.EmailField(blank=True, null=True)
    contact_email = models.CharField(max_length=50, blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)



    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return f'{self.id} {self.partnering_end}'