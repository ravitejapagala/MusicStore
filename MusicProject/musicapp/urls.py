from django.urls import path
from . views import MusicTotorial,basepage

urlpatterns = [
    path('music',MusicTotorial,name="musicname"),
    path('',basepage,name='base')
]