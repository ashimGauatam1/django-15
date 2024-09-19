from django.urls import path
from .views.main_view import home,create_blog,single_blog
from .views.auth_view import login,register
urlpatterns = [
    path('',home),
    path('login',login),
    path('register',register),
    path('create_blog',create_blog),
    path('single_blog/<int:pk>',single_blog),
]
