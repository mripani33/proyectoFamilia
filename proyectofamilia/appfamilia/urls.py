from django.urls import path
from appfamilia.views import *

urlpatterns = [
    path('',inicio),
    path('familiares/',familiares)
]