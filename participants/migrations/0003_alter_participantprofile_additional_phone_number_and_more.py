# Generated by Django 5.0.2 on 2024-03-04 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participants', '0002_alter_participantprofile_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participantprofile',
            name='additional_phone_number',
            field=models.CharField(blank=True, help_text='Доп. номер телефона', max_length=255),
        ),
        migrations.AlterField(
            model_name='participantprofile',
            name='phone_number',
            field=models.CharField(help_text='Номер телефона', max_length=255),
        ),
    ]
