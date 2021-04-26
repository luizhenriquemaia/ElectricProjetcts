from django.db import models
from client.models import b01Clients, b02Address


class c01Project(models.Model):
    id = models.IntegerField(primary_key=True)
    client = models.ForeignKey(b01Clients, on_delete=models.CASCADE)
    address = models.ForeignKey(b02Address, on_delete=models.CASCADE)
    description = models.CharField(max_length=250, null=True)
    observation = models.CharField(max_length=500, null=True)
    initial_date = models.DateField(auto_now=False, auto_now_add=True)
    objects = models.Manager()