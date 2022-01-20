from django.urls import path

from . import views

urlpatterns = [
    path('derp', views.derp, name='derp'),
    path('env', views.env_check, name='env_check'),
    path('', views.index, name='index'),
]