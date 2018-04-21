from django.urls import path

from . import views

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('contact_initial/', views.contact_initial, name='contact_initial')
  ]