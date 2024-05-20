from django.db import models
from django.contrib.auth.models import User
from product.models import Product
from address_book.models import Address


class SerialNumber(models.Model):
    """ Docstring """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    link_product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    link_partnering_end = models.ForeignKey(Address, on_delete=models.CASCADE, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    serial_number = models.CharField(max_length=50)

    class Meta:
        """ Docstring """
        ordering = ['-updated_at']

    def __str__(self):
        return self.serial_number