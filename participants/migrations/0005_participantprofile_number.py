# Generated by Django 5.0.2 on 2024-04-08 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participants', '0004_alter_participantprofile_additional_phone_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='participantprofile',
            name='number',
            field=models.IntegerField(default=1),
        ),
    ]
