from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views.main_view import home, create_blog, single_blog
from .views.auth_view import login, register

urlpatterns = [
    path("", home, name="home"), 
    path("register/", register, name="register"), 
    path("login/", login, name="login"),
    path("create_blog/", create_blog, name="create_blog"),
    path("single_blog/<int:pk>/", single_blog, name="single_blog"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
