from django.db import models

from clients.models import Order


class Bottle(models.Model):
    # address = models.CharField(max_length=255)
    volume = models.IntegerField(default=10)
    maker = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    in_stock = models.BooleanField(default=True)

    orders = models.ManyToManyField(
        to=Order,
        null=True, blank=True,
        verbose_name='Orders',
        related_name='bottles'
    )

    def __str__(self):
        return f'{self.maker} ({self.volume} l.)'


class BottlesCount(models.Model):
    bottle = models.ForeignKey(
        to=Bottle,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='bottle_count')
    count = models.IntegerField(default=0)
    order = models.ForeignKey(
        to=Order,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='order'
    )

    def __str__(self):
        return f'name: {self.bottle} - count: {self.count}'
