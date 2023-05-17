from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import CategoryAPIView,ProductAPIView

from . import views

urlpatterns = [
    path("", views.produit, name="produit"),
    path('Fournisseur/',views.fournisseur,name="Fournisseur"),
    path ('register/',views.register,name='register'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('login/',auth_views.LoginView.as_view(template_name='registration/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name = 'logout'),
    path('api/category/',views.CategoryAPIView.as_view()),
    path('api/product/',views.ProductAPIView.as_view()),
    
]