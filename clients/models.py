from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    active = models.BooleanField(default=True, verbose_name="Active")
    bottles_ordered = models.IntegerField(default=0)
    photo = models.ImageField(
        verbose_name='Photo',
        upload_to='photos',
        null=True,
        blank=True
    )
    # description = models.TextField(null=True, blank=True)


