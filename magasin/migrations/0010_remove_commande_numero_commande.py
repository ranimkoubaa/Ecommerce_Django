# Generated by Django 5.0.2 on 2024-03-10 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0009_commande_numero_commande'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commande',
            name='numero_commande',
        ),
    ]
