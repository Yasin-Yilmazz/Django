from django.urls import path
from .views import yase

urlpatterns = [
    path("",yase)
]