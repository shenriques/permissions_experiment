from django.db import models

class ClientOrganisation(models.Model):
    name = models.CharField(max_length=255)

class Project(models.Model):
    name = models.CharField(max_length=255)
    data = models.JSONField()
    organisation = models.ForeignKey(
        ClientOrganisation, related_name="projects", on_delete=models.CASCADE
    )

