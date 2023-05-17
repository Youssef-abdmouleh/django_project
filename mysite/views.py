from django.shortcuts import render
from django.template import loader
from magasin.views import fournisseur

def index(request):
    context={'val':"Menu Acceuil"}
    return render(request,'acceuil.html',context )