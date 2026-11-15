from django.urls import path
from .views import health2

urlpatterns = [
    path("", health2, name="health2"),
]