from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('search/', views.search, name='search'),
    path('allproducts/', views.search_all, name='all'),
    path('cart/', views.cart, name='cart'),
    path('base/', views.cart, name='base'),
    path('edit_products/', views.edit_products, name='edit'),
    path('add/', views.add_products, name='add')
]
