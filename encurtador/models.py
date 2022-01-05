from django.db import models
import random

# Create your models here.

class Encurtador(models.Model):
    link_original = models.CharField(unique=True, max_length=500, blank=False, null=False)
    link_encurtado = models.CharField(max_length=10, blank=True, null=True)


    def __str__(self):
        return self.link_encurtado

    def save(self, *args, **kwargs):
        self.link_encurtado = str(random.randint(0, 999999999))

        return super().save()