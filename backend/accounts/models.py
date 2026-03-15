from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Permission(models.Model):
    permission_code = models.CharField(max_length=100, unique=True)
    permission_description = models.TextField(blank=True)

    def __str__(self):
        return self.permission_code

class User(AbstractUser):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Manager','Manager'),
        ('Agent', 'Agent'),
        ('Customer', 'Customer')
    ]

    role_label = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Customer')

    permissions = models.ManyToManyField(Permission, blank=True)