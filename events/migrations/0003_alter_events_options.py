# Generated by Django 4.2.7 on 2023-11-29 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_rename_event_events'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='events',
            options={'verbose_name': 'Мероприятие', 'verbose_name_plural': 'Мероприятия'},
        ),
    ]
