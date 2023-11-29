from django.shortcuts import render
from .models import Events


def events(request):
    current_events = Events.objects.order_by('-date')
    return render(request, 'events/events.html', {'current_events': current_events})
