from django.db import models

class User(models.Model) :
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    societe = models.CharField(max_length=100)
    adresse = models.CharField(max_length=255)
    cp = models.CharField(max_length=20)
    ville = models.CharField(max_length=60)
    pathlogo = models.CharField(max_length=255)
    pseudo = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self) :
        return self.pseudo