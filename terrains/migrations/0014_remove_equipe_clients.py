# Generated by Django 5.0.4 on 2024-04-19 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('terrains', '0013_remove_client_equipe_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipe',
            name='clients',
        ),
    ]
