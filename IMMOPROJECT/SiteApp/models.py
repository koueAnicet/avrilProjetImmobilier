from django.db import models

# Create your models here.
class Site(models.Model):
    code_site = models.CharField(max_length=50)
    libele_site = models.CharField(max_length=50)
    superfici_site = models.FloatField()

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(null=True)
    date_delete = models.DateTimeField(auto_now=True)

class Localite(models.Model):
    num_localite =models.CharField(max_length=50)
    nom_localite = models.CharField(max_length=50)
    long_localite =  models.FloatField()
    lat_localite =  models.FloatField()

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(null=True)
    date_delete = models.DateTimeField(auto_now=True)

class Propitaire(models.Model):
    nom_acquereur = models.CharField(max_length=50)
    prenom_acquereur = models.CharField(max_length=100)
    date_naiss_acquereur = models.DateField(null=True, blank=True)
    nationa_acquereur = models.CharField(max_length=20)
    tel_acquereur = models.models.CharField( max_length=10)
    email_acquereur = models.models.EmailField( max_length=254)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(null=True)
    date_delete = models.DateTimeField(auto_now=True)

class DroitFoncier(models.Model):
    code_droit_foncier = models.CharField(max_length=50)
    libele_droit_foncier = models.CharField(max_length=100)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(null=True)
    date_delete = models.DateTimeField(auto_now=True)

