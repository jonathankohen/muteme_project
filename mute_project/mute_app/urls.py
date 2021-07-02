from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("increase", views.increase, name="increase"),
    path("decrease", views.decrease, name="decrease"),
    path("mute", views.mute, name="mute"),
]
