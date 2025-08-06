from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class PlanSolid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card = models.CharField(max_length=100)
    buyTime = models.DateTimeField(default=timezone.now)

class PlanPremium(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card = models.CharField(max_length=100)
    buyTime = models.DateTimeField(default=timezone.now)
# Create your models here.
