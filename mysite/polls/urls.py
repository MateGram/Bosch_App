from django.urls import path

from . import views

# Setting index call
urlpatterns = [
    path('', views.index, name='index'),
]