# Generated by Django 5.0.4 on 2024-04-18 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('terrains', '0006_remove_reservation_client_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='client',
            new_name='client_id',
        ),
        migrations.RenameField(
            model_name='reservation',
            old_name='terrain',
            new_name='terrain_id',
        ),
    ]
