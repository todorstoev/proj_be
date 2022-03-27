from django.db import models
from django.contrib.auth.models import User


def upload_path(self, filename):
    return '/'.join([str(self.name), filename])


class Form(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    file = models.ImageField(blank=True, null=True, upload_to=upload_path)

    def __str__(self):
        return self.name
