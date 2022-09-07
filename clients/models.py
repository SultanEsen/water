from django.db import models
from django.contrib.auth.models import User

# from core.models import Bottle


class Client(models.Model):
    user = models.OneToOneField(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='client'
    )
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

    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    client = models.ForeignKey(
        to=Client,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='order'
    )
    # bottle = models.ForeignKey(
    #     to=Bottle,
    #     null=True,
    #     blank=True,
    #     on_delete=models.SET_NULL,
    #     related_name='order'
    # )
    created_at = models.DateTimeField(
        verbose_name="Date and time of creation of order",
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name="Date and time of update of order",
        auto_now=True,
    )
    description = models.TextField(null=True, blank=True)
    name = models.CharField(max_length=255, help_text='Enter your full name')
    contacts = models.CharField(null=True, blank=True, max_length=255, help_text='Phone number or telegram')
    finished = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.client} - {self.contacts}'

    # class Meta:
    #     verbose_name = "Order"
    #     verbose_name_plural = "Orders"
