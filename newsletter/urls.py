from django.urls import path
from . import views

urlpatterns = [
    path('subscribed', views.subscribed, name='subscribed'),
]
