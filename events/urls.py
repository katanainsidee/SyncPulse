from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.events, name='events'),
    path('<int:event_id>/', views.event_detail, name='event_detail'),
    path('<int:event_id>/add_participant', views.add_participant, name='add_participant'),
    path('<int:event_id>/add_participant/delete_participant<int:participant_id>', views.delete_participant, name='delete_participant'),
    path('<int:event_id>/add_participant/update_color<int:participant_id>', views.update_color, name='update_color'),
    path('<int:event_id>/add_participant/save_csv', views.save_csv, name='save_csv')
]
