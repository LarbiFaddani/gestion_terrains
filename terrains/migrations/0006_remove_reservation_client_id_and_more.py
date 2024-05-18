# Generated by Django 5.0.4 on 2024-04-18 20:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terrains', '0005_alter_client_equipe_id_alter_facture_reservations_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='client_id',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='terrain_id',
        ),
        migrations.AddField(
            model_name='reservation',
            name='client',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='terrains.client'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='terrain',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='terrains.terrain'),
        ),
    ]
