from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.events, name='events'),
    path('events/<int:event_id>/', views.event_detail, name='event_detail'),
]