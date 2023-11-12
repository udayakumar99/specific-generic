from django.urls import path 
from shailesh.views import *

app_name='anything'

urlpatterns=[
    path('cool/',cool,name='shaile.html')
]