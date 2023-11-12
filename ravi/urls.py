from django.urls import path
from ravi.views import *

app_name='something'

urlpatterns=[
    path('urgent/',urgent,name='ravi.html')
]