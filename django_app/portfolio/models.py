from django.db import models

# Create your models here
class ContactInfo(models.Model):
    Name = models.CharField(max_length=100, blank= False)
    Email = models.EmailField(max_length=100, blank= False)
    Message = models.TextField(max_length=500)