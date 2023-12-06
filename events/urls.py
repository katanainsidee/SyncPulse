from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.events, name='events'),
    path('<int:event_id>/', views.event_detail, name='event_detail'),
    path('<int:event_id>/add_participant', views.add_participant, name='add_participant')
]