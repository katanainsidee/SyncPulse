from django.shortcuts import render, redirect
from django.contrib import messages
from main.forms import AddEventForm


def index(request):
    return render(request, 'main/index.html')


def add_event(request):
    return render(request, 'main/add_event_page.html')


def add_event(request):
    error = ''
    if request.method == 'POST':
        form = AddEventForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Мероприятие успешно добавлено')
            return redirect('success_page')
        else:
            error = 'Поля заполнены неверно'
    else:
        form = AddEventForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'main/add_event_page.html', data)


def success_page(request):
    return render(request, 'main/success_page.html')


def back_on_main_page(request):
    return render(request, 'main/index.html')