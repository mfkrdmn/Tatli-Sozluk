from django.urls import path
from . import views

urlpatterns = [
    path('newentry', views.entry_page, name='entrypage'),
    path('newentry', views.search, name='search'),

]