# Generated by Django 5.0.4 on 2024-04-18 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terrains', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipe',
            name='clients',
        ),
        migrations.AddField(
            model_name='client',
            name='equipes',
            field=models.ManyToManyField(related_name='clients', to='terrains.equipe'),
        ),
    ]
