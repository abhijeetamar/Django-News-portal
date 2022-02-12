from django.urls import path
from.views import *

urlpatterns = [
    path('',index),
    path('movies',moviesinfo),
    path('sports',sportsinfo),
    path('politics',politicsinfo),
]