# Generated by Django 5.0.2 on 2024-04-15 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0012_alter_commande_totalcde'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commande',
            name='totalCde',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
    ]
