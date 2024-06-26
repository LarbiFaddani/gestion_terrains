# Generated by Django 5.0.4 on 2024-04-18 20:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terrains', '0004_terrain_administrateur'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='equipe_id',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='terrains.equipe'),
        ),
        migrations.AlterField(
            model_name='facture',
            name='reservations',
            field=models.OneToOneField(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='terrains.reservation'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='client_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='terrains.client'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='terrain_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='terrains.terrain'),
        ),
    ]
