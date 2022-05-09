from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('play',views.play,name='play'),
    path('playback',views.playback,name='playback'),
    path('rep',views.report,name="rep")
]