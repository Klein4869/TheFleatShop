from django.urls import path

from . import views, forms

urlpatterns = [
    path('account/', views.account, name='account'),
    path('account_regist/', views.register, name='register'),
    path('account_login/', views.login, name='login'),
]