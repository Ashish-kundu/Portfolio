from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=120)
    address=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=12)
    date=models.DateTimeField()

    def __str__(self):
        return self.name