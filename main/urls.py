
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index),
    path('events', include('events.urls')),
    path('participants', include('participants.urls'))
]