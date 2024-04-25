# Generated by Django 5.0.4 on 2024-04-19 15:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terrains', '0011_remove_client_equipe_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='equipe_id',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='terrains.equipe'),
        ),
    ]