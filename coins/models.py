from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Cripto(models.Model):
    cripto_pessoa = models.ForeignKey(User, on_delete=models.CASCADE)
    cripto_name = models.CharField(max_length=50)
    cripto_symbol = models.CharField(max_length=10)
    cripto_value = models.FloatField()
    cripto_supply = models.IntegerField()
    cripto_creators = models.CharField(max_length=100)
    cripto_description = models.TextField()
    cripto_category = models.CharField(max_length=100)
    cripto_date_insert = models.DateTimeField(default=datetime.now, blank=True)
    cripto_published = models.BooleanField(default=False)
    crito_image = models.ImageField(upload_to='images/%d/%m/%Y/', blank=True)
    objects = models.Manager()

    def __str__(self):
        return self.cripto_name