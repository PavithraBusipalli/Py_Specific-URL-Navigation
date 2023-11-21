from app2.views import *
from django.urls import path

app_name='secondserver'

urlpatterns=[
    path('server/',server,name='server'),
]