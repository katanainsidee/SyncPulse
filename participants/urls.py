from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.add_user, name='add_user'),
]