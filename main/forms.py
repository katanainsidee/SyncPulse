
from events.models import Events
from django.forms import ModelForm, TextInput, NumberInput, DateInput, Textarea


class AddEventForm(ModelForm):
    class Meta:
        model = Events
        fields = ['title', 'description', 'full_text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название мероприятия',
                'id': 'title'
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Краткое описание',
                'id': 'description'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Полное описание',
                'id': 'full_text'
            }),
            "date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата мероприятия (ДД.ММ.ГГГГ)',
                'id': 'date',
                'maxlength': '10'
            })
        }
