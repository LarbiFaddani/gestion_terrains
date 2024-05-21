# Generated by Django 5.0.4 on 2024-05-20 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terrains', '0031_remove_reservation_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='montant_payer',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
