# Generated by Django 5.0.4 on 2024-05-19 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('terrains', '0029_remove_reservation_date_debut_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='heure_fin',
        ),
    ]
