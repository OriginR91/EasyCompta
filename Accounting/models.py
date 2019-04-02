from django.db import models

# Create your models here.
class Facture(models.Model) :
    facture_number = models.CharField(max_length=100, unique=True)
    facture_date = models.DateField()
    