from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class team(models.Model):
    name = models.CharField(max_length=60)
    img = models.ImageField(upload_to='img/', null=True)
    position = models.CharField(max_length=60)
    profile = models.TextField()
    email = models.CharField(max_length=50)
    facebook = models.URLField(max_length=200, null=True)
    twiter = models.URLField(max_length=200, null=True)
    instagram = models.URLField(max_length=200, null=True)
    linkin = models.URLField(max_length=200, null=True)


class team_detail(models.Model):
    name = models.CharField(max_length=60)
    img = models.ImageField(upload_to='img/', null=True)
    position = models.CharField(max_length=60)
    profile = models.TextField()
    email = models.CharField(max_length=50)
    facebook = models.URLField(max_length=200, null=True)
    twiter = models.URLField(max_length=200, null=True)
    instagram = models.URLField(max_length=200, null=True)
    linkin = models.URLField(max_length=200, null=True)