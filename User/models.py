from django.contrib.auth.models import User
from django.db import models

class Profil(models.Model) :
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    societe = models.CharField(max_length=100)
    adresse = models.CharField(max_length=255)
    cp = models.CharField(max_length=20)
    ville = models.CharField(max_length=60)
    pathlogo = models.CharField(max_length=255)

    def __str__(self) :
        return "{} - {} - {} - {} - {} - {} - {} - {} - {} - {}".format(
            self.user.username,
            self.user.password,
            self.user.email,
            self.user.last_name,
            self.user.first_name,
            self.societe,
            self.adresse,
            self.cp,
            self.ville,
            self.pathlogo
        )