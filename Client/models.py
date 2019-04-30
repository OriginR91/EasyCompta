from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Client(models.Model) :
    client_nom = models.CharField(max_length=150)
    client_siret = models.CharField(max_length=30)
    client_adresse = models.CharField(max_length=255)
    client_cp = models.CharField(max_length=20)
    client_ville = models.CharField(max_length=60)
    username = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) :
        return "{} {} {} {} {}".format(
            self.client_nom,
            self.client_siret,
            self.client_adresse,
            self.client_cp,
            self.client_ville
        )