from django.shortcuts import render, get_object_or_404, redirect
from .models import Events
from .forms import ParticipantForm
from django.http import JsonResponse
from django.urls import reverse
import json


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
            # Проверяем, есть ли уже участник с таким номером телефона
            existing_participant = event.participant_set.filter(phone_number=participant.phone_number).first()
            if existing_participant:
                error = 'Участник с таким номером телефона уже зарегистрирован на мероприятии'
            else:
                participant.event = event
                participant.save()
                if request.headers.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
                    return JsonResponse({'redirect_url': reverse('event_detail', args=[event.id])})
                else:
                    return redirect('event_detail', event_id=event.id)
        else:
            error = 'Поля заполнены неверно'
    else:
        form = ParticipantForm()

    if request.headers.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        return JsonResponse({'error': error})
    else:
        return render(request, 'events/add_participant.html', {'form': form, 'event': event, 'error': error})




