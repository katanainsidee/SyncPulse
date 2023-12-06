from django.shortcuts import render, get_object_or_404, redirect
from .models import Events
from .forms import ParticipantForm


def events(request):
    current_events = Events.objects.order_by('-date')
    return render(request, 'events/events.html', {'current_events': current_events})


def event_detail(request, event_id):
    event = get_object_or_404(Events, pk=event_id)
    return render(request, 'events/event_detail.html', {'event': event})


def add_participant(request, event_id):
    event = Events.objects.get(pk=event_id)
    error = ''
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            participant = form.save(commit=False)
            participant.event = event
            participant.save()
            return redirect('event_detail', event_id=event.id)
        else:
            error = 'Поля заполнены неверно'
    else:
        form = ParticipantForm()

    return render(request, 'events/add_participant.html', {'form': form, 'event': event, 'error': error})