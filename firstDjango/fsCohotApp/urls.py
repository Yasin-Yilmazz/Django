from django.urls import path

from .views import fshome
urlpatterns = [
    path("",fshome),
]
