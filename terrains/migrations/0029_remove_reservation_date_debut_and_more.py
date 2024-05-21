# Generated by Django 5.0.4 on 2024-05-19 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terrains', '0028_remove_reservation_client_id_remove_equipe_clients_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='date_debut',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='date_fin',
        ),
        migrations.AddField(
            model_name='reservation',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='heure_debut',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='heure_fin',
            field=models.TimeField(blank=True, null=True),
        ),
    ]