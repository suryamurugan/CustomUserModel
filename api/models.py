from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    usn = models.TextField(max_length=10, blank=True)
    department = models.TextField(max_length=500, blank=True)