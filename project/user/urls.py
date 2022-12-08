from django.urls import path
from . import views

urlpatterns = [
    path('user', views.user_page, name='user_page'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('contract', views.contract, name='contract'),
]