from django.contrib import admin
from .models import Events, Participant
# Register your models here.


@admin.register(Events)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')  # Используем 'title' вместо 'name'


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'event_name')  # Используем 'first_name' и 'last_name'
    list_filter = ('event',)

    def event_name(self, obj):
        return obj.event.title if obj.event else None  # Используем 'title' вместо 'name'
#
    event_name.short_description = 'Event Name'
#
     # Добавляем поля для отображения в административной панели
    list_display_links = ('first_name', 'last_name')

    def get_list_display(self, request):
        return super().get_list_display(request) + ('event_name',)

    #Определение фильтра по мероприятию
    def event(self, obj):
        return obj.event.title if obj.event else None

    event.admin_order_field = 'event__title'  # Используем 'title' вместо 'name'
    event.short_description = 'Event'