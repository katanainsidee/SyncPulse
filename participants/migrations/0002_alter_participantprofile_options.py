# Generated by Django 4.2.7 on 2023-12-06 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('participants', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='participantprofile',
            options={'verbose_name': 'Участник', 'verbose_name_plural': 'Участники'},
        ),
    ]
