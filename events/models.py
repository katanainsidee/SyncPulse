from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Events(models.Model):
    title = models.CharField('Название', max_length=155)
    description = models.CharField('Описание', max_length=250)
    full_text = models.TextField('Мероприятие')
    date = models.DateField('Дата мероприятия')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'


class Participant(models.Model):
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    district = models.CharField(max_length=255, blank=True)
    street = models.CharField(max_length=255, blank=True)
    house_number = models.PositiveIntegerField(blank=True)
    building = models.CharField(max_length=255, blank=True)
    apartment_number = models.PositiveIntegerField(blank=True)
    phone_number = models.CharField(max_length=18)
    additional_phone_number = models.CharField(max_length=18, blank=True)
    color = models.CharField(max_length=20, default='white')
    number = models.IntegerField(default=1)
