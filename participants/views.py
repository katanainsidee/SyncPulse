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
    error = ''
    if request.method == 'POST':
        form = ParticipantProfileForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            if ParticipantProfile.objects.filter(phone_number=phone_number).exists():
                error += 'Пользователь с таким номером телефона уже зарегистрирован'
            else:
                form.save()
                messages.success(request, 'Новый пользователь успешно добавлен')
                return redirect('success_page')
        else:
            error += 'Поля заполнены неверно'

    form = ParticipantProfileForm(request.POST or None)
    data = {
        'form': form,
        'error': error
    }

    return render(request, 'participants/participants.html', data)


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
