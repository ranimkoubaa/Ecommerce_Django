# Generated by Django 5.0.2 on 2024-02-23 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0003_categorie_alter_produit_image_produit_categorie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produit',
            name='image',
        ),
        migrations.AlterField(
            model_name='produit',
            name='description',
            field=models.TextField(default='Non définie'),
        ),
        migrations.AlterField(
            model_name='produit',
            name='libelle',
            field=models.CharField(max_length=100),
        ),
    ]
