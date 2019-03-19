from django.db import models

class User(models.Model) :
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField(max_length=70, null=False, unique=True)
    societe = models.CharField(max_length=100)
    adresse = models.CharField(max_length=255)
    cp = models.CharField(max_length=20)
    ville = models.CharField(max_length=60)
    pathlogo = models.CharField(max_length=255)
    pseudo = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self) :
        return "{} - {} - {} - {} - {} - {} - {} - {} - {}".format(
            self.nom,
            self.prenom,
            self.email,
            self.societe,
            self.adresse,
            self.cp,
            self.ville,
            self.pathlogo,
            self.pseudo,
            self.password
        )