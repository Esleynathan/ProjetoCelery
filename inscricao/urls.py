from django.urls import path
from . import views


urlpatterns = [
    path('', views.inscricao, name='inscricao')
]
