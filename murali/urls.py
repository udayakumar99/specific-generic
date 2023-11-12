from django.urls import path
from murali.views import *

app_name='something'

urlpatterns=[
    path('cvil/',cvil,name='murali.html')
]