# Generated by Django 5.0.2 on 2024-02-23 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0004_remove_produit_image_alter_produit_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='img',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]