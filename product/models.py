from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    """ Docstring """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_at = models.DateField(auto_now=True)
    product_name = models.CharField(max_length=50)
    serial_number_prefix = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        """ Docstring """
        ordering = ['-updated_at']
    
    def __str__(self):
        return f'{self.id} {self.product_name}'
