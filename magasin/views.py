from .models import Produit, Categorie
from django.shortcuts import redirect
from django.shortcuts import render
from .templates import magasin
from .forms import *
from rest_framework.views import APIView
from .serializers import CategorySerializer,ProductSerializer
from rest_framework.response import Response
from rest_framework import viewsets





# Create your views here.
def produit(request): 
    list=Produit.objects.all()
    return render(request,'magasin/vetrine.html',{'list':list})


def fournisseur(request):
    list=fournisseur.objects.all()
    return render(request,'magasin/fournisseur.html',{'list':list})

def register(request):
    if request.method=='post':
        form=UserCreationForm(request.post)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password1')
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,f'Coucou{username},Votre compte a ete cree avec succes !')
            return redirect('acceuil')
    else:
        form=UserCreationForm()
    return render(request,'registration/register.html',{'form':form})



class CategoryAPIView(APIView):
    def get(self, *args, **kwargs):
        categories = Categorie.objects.all()
        Cserializer = CategorySerializer(categories, many=True)
        return Response(Cserializer.data)


class ProductAPIView(APIView):
    def get(self, *args, **kwargs):
        produits = Produit.objects.all()
        Pserializer = ProductSerializer(produits, many=True)
        return Response(Pserializer.data)









class ProductViewset(viewsets.ReadOnlyModelViewSet):

    serializer_class = ProductSerializer
    def get_queryset(self):
        queryset = Produit.objects.all()
        category_id = self.request.GET.get('category_id')
        if category_id:
            queryset = queryset.filter(categorie_id=category_id)
        return queryset
