from django.forms import ModelForm
from .models import Produit
from .models import Fournisseur
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class ProduitForm(ModelForm):
    class Meta :
        model = Produit 
        fields = "__all__" #pour tous les champs de la table 
        #fields=['libelle','description'] #pour qulques champs

class FournisseurForm(ModelForm):
    class meta : 
        model=Fournisseur
        fields ="__all__"
        


class UserRegistarationForm (UserCreationForm):
    first_name=forms.CharField(label='Prenom')
    last_name=forms.CharField(label='Nom')
    email=forms.EmailField(label='Adresse e-mail')

    class meta (UserCreationForm.Meta):
        model=User
        field=UserCreationForm.Meta.fields+('first_name','last_name','email')