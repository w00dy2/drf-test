from django.db import models

class Addresses(models.Model):
    name = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=13)
    address = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:  # The "M" should be capitalized
        ordering = ['created']
