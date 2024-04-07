import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Events, Participant
from .forms import ParticipantForm, ParticipantColorForm
from django.http import JsonResponse
from django.urls import reverse


@login_required
def events(request):
    current_events = Events.objects.order_by('-date')
    return render(request, 'events/events.html', {'current_events': current_events})


@login_required
def event_detail(request, event_id):
    event = get_object_or_404(Events, pk=event_id)
    return render(request, 'events/event_detail.html', {'event': event})


@login_required
def add_participant(request, event_id):
    event = Events.objects.get(pk=event_id)
    participants_list = Participant.objects.filter(event=event)
    error = ''
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            participant = form.save(commit=False)
            existing_participant = event.participant_set.filter(phone_number=participant.phone_number).first()
            if existing_participant:
                error = 'Участник с таким номером телефона уже зарегистрирован на мероприятии'
            else:
                participant.event = event
                participant.save()
                if request.headers.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
                    return JsonResponse({'redirect_url': reverse('event_detail', args=[event.id])})
                else:
                    return redirect('add_participant', event_id)
        else:
            error = 'Поля заполнены неверно'

    else:
        form = ParticipantForm()

    if request.headers.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        return JsonResponse({'error': error})
    else:
        return render(request, 'events/add_participant.html', {'form': form,  'event': event, 'error': error, 'participants_list': participants_list})


@login_required
def delete_participant(request, event_id, participant_id):
    participant = Participant.objects.get(event=event_id, id=participant_id)
    participant.delete()
    return redirect('add_participant', event_id)


@login_required
def update_color(request, event_id, participant_id):
    print(f'Работаем! event_id - {event_id}, request - {request.method}')
    if request.method == 'POST':
        event = Events.objects.get(pk=event_id)
        participant = Participant.objects.get(event=event, id=participant_id)

        # Получаем данные из тела запроса JSON
        data = json.loads(request.body)
        color = data.get('color')

        print(f'цвет - {color}')

        participant.color = color
        participant.save()
        print('Сейчас обновимся')
        return redirect('add_participant', event_id)

    return JsonResponse({'error': 'Метод запроса не разрешен'}, status=405)
