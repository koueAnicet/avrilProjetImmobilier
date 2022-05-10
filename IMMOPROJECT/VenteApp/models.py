from django.db import models

# Create your models here.
class TypeLogement(models.Model):
    code_typ_logement = models.CharField(max_length=50)
    libele_typ_logement = models.CharField(max_length=50)
    cout_typ_logement = models.IntegerField()
    date_crea_typ_logement =models.DateField()

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(null=True)
    date_delete = models.DateTimeField(auto_now=True)

class Logement(models.Model):
    num_logement = models.CharField(max_length=50)
    libele_logement = models.CharField(max_length=50)
    cout_logement = models.IntegerField()
    date_crea_logement =models.DateField()

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(null=True)
    date_delete = models.DateTimeField(auto_now=True)

class Cite(models.Model):
    code_cite = models.CharField(max_length=50)
    nom_cite = models.CharField(max_length=50)
    #locisation_cite = models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE) 

    date_add = models.DateTimeField()
    date_update = models.DateTimeField()
    date_delete = models.DateTimeField()


class Acquereur(models.Model):
    nom_acquereur = models.CharField(max_length=50)
    prenom_acquereur = models.CharField(max_length=100)
    date_naiss_acquereur = models.DateField(null=True, blank=True)
    nationa_acquereur = models.CharField(max_length=20)
    tel_acquereur = models.models.CharField( max_length=10)
    email_acquereur = models.models.EmailField( max_length=254)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(null=True)
    date_delete = models.DateTimeField(auto_now=True)

class Infrastructure(models.Model):
    code_infrast = models.CharField(max_length=50)
    nom_infrast = models.CharField(max_length=50)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(null=True)
    date_delete = models.DateTimeField(auto_now=True)

class Site(models.Model):
    code_site = models.CharField(max_length=50)
    libele_site = models.CharField(max_length=50)
    superfici_site = models.FloatField()

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(null=True)
    date_delete = models.DateTimeField(auto_now=True)


