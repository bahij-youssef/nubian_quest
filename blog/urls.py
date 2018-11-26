from django.urls import path

from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<str:slug>', views.single_post, name='single_post'),
]
