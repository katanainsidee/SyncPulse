
from .models import Participant
from django.forms import ModelForm, TextInput, NumberInput, DateInput, Select


class ParticipantForm(ModelForm):
    class Meta:
        model = Participant
        fields = ['first_name', 'last_name', 'patronymic', 'date_of_birth', 'district', 'street', 'house_number',
                  'building', 'apartment_number', 'phone_number', 'additional_phone_number']

        widgets = {
            "first_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя',
                'id': 'first_name'
            }),
            "last_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия',
                'id': 'last_name'
            }),
            "patronymic": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Отчество',
                'id': 'patronymic'
            }),
            "date_of_birth": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата рождения (ДД.ММ.ГГГГ)',
                'id': 'date_of_birth',
                'maxlength': '10'
            }),
            "district": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Район',
                'id': 'district'
            }),
            "street": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Улица',
                'id': 'street'
            }),
            "house_number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дом',
                'id': 'house_number'
            }),
            "building": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Корпус/строение',
                'id': 'building'
            }),
            "apartment_number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Квартира',
                'id': 'apartment_number'
            }),
            "phone_number": TextInput(attrs={
                'maxlength': "18",
                'class': 'form-control',
                'placeholder': 'Номер телефона +7 (999) 999-99-99',
                'id': 'phone_number'
            }),
            "additional_phone_number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Доп. информация',
                'id': 'additional_phone_number',
                'maxlength': '30'
            })
        }


class ParticipantColorForm(ModelForm):
    class Meta:
        model = Participant
        fields = ['color']
        widgets = {
            'color': Select(choices=[
                ('white', 'Белый'),
                ('yellow', 'Желтый'),
                ('green', 'Зеленый'),
                ('red', 'Красный')
            ])
        }