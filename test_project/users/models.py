from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Developer', 'Developer'),
        ('Consultant', 'Consultant'),
        ('Client', 'Client'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    organisation = models.ForeignKey(
        'projects.ClientOrganisation', 
        null=True, blank=True, 
        on_delete=models.SET_NULL,
        related_name='users'
    )

    def __str__(self):
        return f"{self.username} ({self.role})"
