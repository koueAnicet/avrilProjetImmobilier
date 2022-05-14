from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('souscription/', views.souscription, name="souscription"),
    path('proprietaire', views.proprietaire, name="proprietaire"),
    path('contact', views.contact, name="contact"),
    path('vente/', views.vent, name="vente"),
    path('site/', views.site, name="site"),
    path('localite/', views.localite, name="localite"),
]
