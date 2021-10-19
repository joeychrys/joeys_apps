from django.db import models


# Create your models here.
class NewsPost(models.Model):
    version = models.CharField(max_length=100)
    description = models.TextField()
