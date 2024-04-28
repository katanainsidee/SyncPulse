from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class ParticipantProfile(models.Model):
    first_name = models.CharField(max_length=255, help_text='Имя', blank=True)
    last_name = models.CharField(max_length=255, help_text='Фамилия', blank=True)
    patronymic = models.CharField(max_length=255, help_text='Отчество', blank=True)
    date_of_birth = models.DateField(help_text='Дата рождения', blank=True)
    district = models.CharField(max_length=255, help_text='Район', blank=True)
    street = models.CharField(max_length=255, help_text='Улица', blank=True)
    house_number = models.CharField(max_length=255, help_text='Номер дома', blank=True)
    building = models.CharField(max_length=255, help_text='Корпус/строение', blank=True)
    apartment_number = models.PositiveIntegerField(help_text='Квартира', blank=True)
    phone_number = models.CharField(max_length=18, help_text='Номер телефона', blank=True)
    additional_phone_number = models.CharField(max_length=18, help_text='Доп. номер телефона', blank=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.patronymic} {self.phone_number}"

    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'