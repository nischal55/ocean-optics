from django.urls import path
from shop import views

urlpatterns = [
    path('', views.index, name='home'),
    path('services', views.services, name='services'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('search', views.search, name='search'),
]
