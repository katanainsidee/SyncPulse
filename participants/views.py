from django.shortcuts import render, redirect
from .forms import ParticipantProfileForm
from .models import ParticipantProfile


# def add_user(request):
#     if request.method == 'POST':
#         form = ParticipantProfileForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('success_page')  # Замените 'success_page' на URL успешной страницы
#     else:
#         form = ParticipantProfileForm()
#
#     return render(request, 'participants/participants.html', {'form': form})

def add_user(request):
    error = ''
    if request.method == 'POST':
        form = ParticipantProfileForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Поля заполнены неверно'

    form = ParticipantProfileForm()
    data = {
        'form': form,
        'error': error
    }

    return render(request, 'participants/participants.html', data)

