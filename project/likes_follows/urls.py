from django.urls import path
from . import views


urlpatterns = [
    path('liked_comments', views.users_liked_comments, name='users_liked_comments'),
]