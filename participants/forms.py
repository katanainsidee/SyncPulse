
from .models import ParticipantProfile
from django.forms import ModelForm, TextInput, NumberInput, DateInput


class ParticipantProfileForm(ModelForm):
    class Meta:
        model = ParticipantProfile
        fields = ['first_name', 'last_name', 'patronymic', 'date_of_birth', 'district', 'street', 'house_number', 'building', 'apartment_number', 'phone_number', 'additional_phone_number']

        widgets = {
            "first_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя',
                'id': 'auto_check'
            }),
            "last_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия',
                'id': 'auto_check'
            }),
            "patronymic": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Отчество',
                'id': 'auto_check'
            }),
            "date_of_birth": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата рождения (ДД.ММ.ГГГГ)',
                'id': 'auto_check'
            }),
            "district": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Район',
                'id': 'auto_check'
            }),
            "street": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Улица',
                'id': 'auto_check'
            }),
            "house_number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дом',
                'id': 'auto_check'
            }),
            "building": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Корпус/строение',
                'id': 'auto_check'
            }),
            "apartment_number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Квартира',
                'id': 'auto_check'
            }),
            "phone_number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер телефона +7XXXXXXXXXX',
                'id': 'auto_check'
            }),
            "additional_phone_number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Доп. номер телефона',
                'id': 'auto_check'
            }),

        }