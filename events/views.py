import csv
import json
import os

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Events, Participant
from .forms import ParticipantForm, ParticipantColorForm
from django.http import JsonResponse, HttpResponse
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
    number = len(participants_list)+1
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
                participant.number = number
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
    if request.method == 'POST':
        event = Events.objects.get(pk=event_id)
        participant = Participant.objects.get(event=event, id=participant_id)
        data = json.loads(request.body)
        color = data.get('color')
        participant.color = color
        participant.save()
        return redirect('add_participant', event_id)

    return JsonResponse({'error': 'Метод запроса не разрешен'}, status=405)


@login_required
def save_csv(request, event_id):
    event = Events.objects.get(pk=event_id)
    participants_list = Participant.objects.filter(event=event)
    file_path = f'{event.id}_отчет.csv'
    with open(file_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter = ";")
        writer.writerow(['№', 'Фамилия', 'Имя', 'Отчество', 'Дата рождения', 'Район', 'Улица', 'Дом', 'Корпус/строение', 'Квартира', 'Номер телефона', 'Доп. номер телефона'])
        for number, participant in enumerate(participants_list, start=1):
            writer.writerow([number, participant.last_name, participant.first_name, participant.patronymic,
                             participant.date_of_birth, participant.district, participant.street,
                             participant.house_number, participant.building, participant.apartment_number,
                             participant.phone_number, participant.additional_phone_number])

    with open(file_path, 'rb') as file:
        file_content = file.read()

    response = HttpResponse(file_content, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename={file_path}.csv'
    os.remove(file_path)
    return response
