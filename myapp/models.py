from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=120)
    email=models.CharField(max_length=100)
    mobile=models.CharField(max_length=100)
    age=models.CharField(max_length=100)
    def __str__(self):
        return f'{self.name},{self.mobile}'
