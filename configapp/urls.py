from django.urls import path
from configapp.views import *

urlpatterns=[
    path('student/', S_01),
    path('kurs/',K_01)
]