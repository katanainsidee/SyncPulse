from django.db import models


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