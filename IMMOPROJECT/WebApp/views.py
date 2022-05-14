from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, "IMMOPROJECT/index.html")

def about(request):
    return render(request, "IMMOPROJECT/contact.html")

def souscription(request):
    return render(request,"IMMOPROJECT/souscription.html" )

def vent(request):
    return render(request, "IMMOPROJECT/vente.html")
def proprietaire(request):
    return render(request, "IMMOPROJECT/proprietraire")
def contact(request):
    return render(request, "IMMOPROJECT/contact.html")

def site(request):
    return render(request, "IMMOPROJECT/site.html")
def localite(request):
    return render(request, "IMMOPROJECT/localite.html")
