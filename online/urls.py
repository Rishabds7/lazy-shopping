from django.urls import path
from . import views
urlpatterns = [
                path('home',views.home,name='home'),
                path('contact', views.contact, name='contact'),
                path('register', views.register, name='register'),
                path('login', views.login, name='login'),
                path('logout', views.Logout, name='logout'),
                path('cart', views.cart, name='cart'),
    ]