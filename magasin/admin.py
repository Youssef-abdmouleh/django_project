from django.contrib import admin

# Register your models here.
from django.urls import path,include 
from . import views
from .models import Produit
from .models import Categorie
admin.site.register(Produit)
admin.site.register(Categorie)

urlpatterns = [ 
path('admin/', admin.site.urls), 
path('magasin/', include('magasin.urls'))
]