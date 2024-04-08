from django.shortcuts import render, redirect
from .forms import ParticipantProfileForm
from .models import ParticipantProfile
from django.http import JsonResponse
import json
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
import os
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def add_user(request):
    participants_list = ParticipantProfile.objects.all()
    number = len(participants_list) + 1
    error = ''
    if request.method == 'POST':
        form = ParticipantProfileForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            if ParticipantProfile.objects.filter(phone_number=phone_number).exists():
                error += 'Пользователь с таким номером телефона уже зарегистрирован'
            else:
                participant = form.save(commit=False)
                participant.number = number
                participant.save()
                messages.success(request, 'Новый пользователь успешно добавлен')
                return redirect('add_user')
        else:
            error += 'Поля заполнены неверно'

    form = ParticipantProfileForm(request.POST or None)
    data = {
        'form': form,
        'error': error,
        'participants_list': participants_list
    }

    return render(request, 'participants/participants.html', data)


def delete(request, participant_id):
    participant = ParticipantProfile.objects.get(id=participant_id)
    participant.delete()
    return redirect('add_user')


@login_required
@receiver(post_save, sender=ParticipantProfile)
@receiver(post_delete, sender=ParticipantProfile)
def update_json_file(sender, instance, **kwargs):
    data = list(ParticipantProfile.objects.values())
    for item in data:
        item['date_of_birth'] = item['date_of_birth'].strftime('%d.%m.%Y')
        item['phone_number'] = str(item['phone_number'])
        item['additional_phone_number'] = str(item['additional_phone_number'])
    with open('events/static/events/data.json', 'w') as f:
        json.dump(data, f)
