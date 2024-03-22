from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from main.forms import AddEventForm


@login_required
def index(request):
    return render(request, 'main/index.html')


@login_required
def add_event(request):
    return render(request, 'main/add_event_page.html')


@login_required
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


@login_required
def success_page(request):
    return render(request, 'main/success_page.html')


@login_required
def back_on_main_page(request):
    return render(request, 'main/index.html')