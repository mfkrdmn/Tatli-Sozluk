from django.urls import path
from . import views

urlpatterns = [
    path('entrypage', views.entry_page, name='entrypage'),
    path('<str:pk>/', views.entry_detail, name='entry_detail'),
]