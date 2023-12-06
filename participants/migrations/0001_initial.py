# Generated by Django 4.2.7 on 2023-12-06 08:35

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ParticipantProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Имя', max_length=255)),
                ('last_name', models.CharField(help_text='Фамилия', max_length=255)),
                ('patronymic', models.CharField(help_text='Отчество', max_length=255)),
                ('date_of_birth', models.DateField(help_text='Дата рождения')),
                ('district', models.CharField(blank=True, help_text='Район', max_length=255)),
                ('street', models.CharField(blank=True, help_text='Улица', max_length=255)),
                ('house_number', models.PositiveIntegerField(blank=True, help_text='Номер дома')),
                ('building', models.CharField(blank=True, help_text='Корпус/строение', max_length=255)),
                ('apartment_number', models.PositiveIntegerField(blank=True, help_text='Квартира')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(help_text='Номер телефона', max_length=128, region=None)),
                ('additional_phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='Доп. номер телефона', max_length=128, region=None)),
            ],
        ),
    ]
