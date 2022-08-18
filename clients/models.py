from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    bottles_ordered = models.IntegerField(default=0)
    # description = models.TextField(null=True, blank=True)

