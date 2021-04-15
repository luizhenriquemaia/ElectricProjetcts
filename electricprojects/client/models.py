from django.db import models

from main.models import a12District


class b01Clients(models.Model):
    id = models.IntegerField(primary_key=True)
    treatment = models.CharField(max_length=30)
    name = models.CharField(max_length=300)
    cnpj = models.CharField(max_length=14)
    description = models.CharField(max_length=300)
    fone = models.CharField(max_length=15)
    email = models.EmailField(null=True)
    objects = models.Manager()


class b02Address(models.Model):
    id = models.IntegerField(primary_key=True)
    client = models.ForeignKey(b01Clients, on_delete=models.CASCADE)
    district = models.ForeignKey(a12District, on_delete=models.CASCADE)
    street = models.CharField(max_length=100)
    complement = models.CharField(max_length=255, blank=True, null=True)
    objects = models.Manager()
