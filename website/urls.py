from django import views
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('get_text', views.get_text, name='get-text')

]
