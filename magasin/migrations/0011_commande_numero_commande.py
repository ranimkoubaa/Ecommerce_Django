# Generated by Django 5.0.2 on 2024-03-10 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0010_remove_commande_numero_commande'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='numero_commande',
            field=models.IntegerField(default=0),
        ),
    ]
