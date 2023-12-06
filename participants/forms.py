
from .models import ParticipantProfile
from django.forms import ModelForm, TextInput, NumberInput, DateInput


class ParticipantProfileForm(ModelForm):
    class Meta:
        model = ParticipantProfile
        fields = ['first_name', 'last_name', 'patronymic', 'date_of_birth', 'district', 'street', 'house_number', 'building', 'apartment_number', 'phone_number', 'additional_phone_number']

        widgets = {
            "first_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            "last_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия'
            }),
            "patronymic": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Отчество'
            }),
            "date_of_birth": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата рождения (ДД.ММ.ГГГГ)',
            }),
            "district": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Район'
            }),
            "street": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Улица'
            }),
            "house_number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дом'
            }),
            "building": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Корпус/строение'
            }),
            "apartment_number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Квартира'
            }),
            "phone_number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер телефона +7XXXXXXXXXX'
            }),
            "additional_phone_number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Доп. номер телефона'
            }),

        }