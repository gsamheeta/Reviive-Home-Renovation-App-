

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Action(models.Model):
    user = models.CharField(max_length=100)
    verb = models.CharField(max_length=100)
    target_id = models.PositiveIntegerField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)