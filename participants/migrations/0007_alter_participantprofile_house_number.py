# Generated by Django 5.0.2 on 2024-04-28 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participants', '0006_remove_participantprofile_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participantprofile',
            name='house_number',
            field=models.CharField(blank=True, help_text='Номер дома', max_length=255),
        ),
    ]