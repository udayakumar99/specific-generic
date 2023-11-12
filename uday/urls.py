from django.urls import path
from uday.views import *
app_name = 'anything'

urlpatterns=[
    path('silent/',silent,name='nani.html')
]