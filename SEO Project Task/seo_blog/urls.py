from django.urls import path
from .views import view_blog

urlpatterns = [
    path("", view_blog, name="view_blog"),
]
