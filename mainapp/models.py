from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserDetails(models.Model):
    userClass = models.ForeignKey(User, on_delete=models.CASCADE)
    currentYear = models.SmallIntegerField()