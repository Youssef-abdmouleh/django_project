"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from magasin import views as mviews
from mysite import views as sviews
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin,auth

from rest_framework import routers
from magasin.views import ProductViewset, CategoryAPIView



router = routers.SimpleRouter()
router.register('produit',viewset=ProductViewset, basename='produit')

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("magasin/", include("magasin.urls")),
    path("produit/",mviews.produit,name="produit"),
    path("", sviews.index, name="index"),
    path('api-auth/',include('rest_framework.urls')),
    path('api/', include(router.urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
