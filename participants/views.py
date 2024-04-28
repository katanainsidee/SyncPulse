from django.shortcuts import render, redirect
from .forms import ParticipantProfileForm
import json
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib import messages
from django.contrib.auth.decorators import login_required
#import pandas as pd
from participants.models import ParticipantProfile



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

# @login_required
# def complete_table(request):
#     file_path = 'D:\SyncPulse\SyncPulse\participants\Книга1.xlsx'
#     excel_data = pd.read_excel(file_path, usecols='A:K')
#     number = 0
#     for index, row in excel_data.iterrows():
#         try:
#             participant_profile = ParticipantProfile(
#                 last_name=row.get('Фамилия', 'НЕ УКАЗАНО'),
#                 first_name=row.get('Имя', 'НЕ УКАЗАНО'),
#                 patronymic=row.get('Отчество', 'НЕ УКАЗАНО'),
#                 date_of_birth=row.get('Дата рождения', '27.04.2024'),
#                 district=row.get('Район', None),
#                 street=row.get('Улица', None),
#                 house_number=row.get('Дом', None),
#                 building=row.get('Корпус/Строение', None),
#                 apartment_number=row.get('Квартира', None),
#                 phone_number=row.get('Номер телефона', '+79999999999'),
#                 additional_phone_number=row.get('Дополнительный номер телефона', None),
#             )
#             participant_profile.save()
#         except Exception as e:
#             print(e)
#             number += 1
#     print(f'{number} человек не добавилось')
#     return redirect('add_user')