
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index),
    path('events', include('events.urls')),
    path('participants', include('participants.urls')),
    path('add_event', views.add_event, name='add_event'),
    path('success', views.success_page, name='success_page'),
    path('back_on_main_page', views.back_on_main_page, name='back_on_main_page')
]
