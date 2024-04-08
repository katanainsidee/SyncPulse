from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.add_user, name='add_user'),
    path('delete_<int:participant_id>', views.delete, name='delete')
]