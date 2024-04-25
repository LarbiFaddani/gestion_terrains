# Generated by Django 5.0.4 on 2024-04-19 16:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terrains', '0016_alter_administrateur_id_alter_client_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facture',
            name='reservations',
        ),
        migrations.AddField(
            model_name='facture',
            name='resservation_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='terrains.reservation'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='Factures',
            field=models.OneToOneField(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='terrains.facture'),
        ),
    ]