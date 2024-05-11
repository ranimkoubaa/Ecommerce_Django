from django.db import models
from datetime import date
from django.urls import reverse
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin

class Fournisseur(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.TextField()
    email = models.EmailField()
    telephone = models.CharField(max_length=8)

    def __str__(self):
        return self.nom

# Create your models here.
class Categorie(models.Model):
    TYPE_CHOICES = [
        ('Al', 'Alimentaire'),
        ('Mb', 'Meuble'),
        ('Sn', 'Sanitaire'),
        ('Ys', 'Vaisselle'),
        ('Vt', 'Vêtement'),
        ('Jt', 'Jouets'),  
        ('Lg', 'Linge de Maison'),
        ('B', 'Bijoux'),
        ('De', 'Décor'),
    ]
    categorie = models.CharField(max_length=50, choices=TYPE_CHOICES, default='Alimentaire')

    def __str__(self):
        return f"Catégorie: {self.categorie}"
  

class Produit(models.Model):
    TYPE_CHOICES = [
        ('em', 'emballé'),
        ('fr', 'Frais'),
        ('cs', 'Conserve')
    ]

    libelle = models.CharField(max_length=100)
    description = models.TextField(default='Non définie')
    prix = models.DecimalField(max_digits=10, decimal_places=3)
    type = models.CharField(max_length=2, choices=TYPE_CHOICES, default='em')
    img = models.ImageField(blank=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, null=True)
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return f"Libellé: {self.libelle}, Description: {self.description}, Prix: {self.prix}, Type: {self.get_type_display()},Image: {self.img},Categorie:{self.categorie} ,Fournisseur {self.fournisseur}"
class ProduitNC(Produit):
        duree_garantie = models.CharField(max_length=100)

        def __str__(self):
            return f"duree_garantie: {self.duree_garantie} ,libellé : {self.libelle} , description : { self.description} , prix : {str(self.prix)} , type: {self.type}, Image: {self.img} ,categorie: {self.categorie} ,fournisseur: {self.fournisseur}"
class Commande(models.Model):
    numero_commande = models.IntegerField(default=0)
    dateCde = models.DateField(null=True, default=date.today)
    totalCde = models.DecimalField(max_digits=10, decimal_places=3)
    produits = models.ManyToManyField(Produit)
    
    
    def calculer_total(self):
        return sum(Produit.prix for Produit in self.produits.all())
    
   # def get_absolute_url(self):
    #    return reverse('supprimer_commande', args=[str(self.id)])
    def delete(self, *args, **kwargs):
        # Récupérer l'identifiant de la commande à supprimer
        numero_commande_a_supprimer = self.numero_commande

        # Supprimer la commande
        super(Commande, self).delete(*args, **kwargs)

        # Mettre à jour les numéros de commande pour les commandes restantes
        Commande.objects.filter(numero_commande__gt=numero_commande_a_supprimer).update(
            numero_commande=models.F('numero_commande') - 1
        )

    def __str__(self):
        return f"Commande {self.numero_commande} - {self.dateCde}"
# models.py dans votre application magasin
from django.db import models
from .models import Produit
from django.contrib.auth.models import User


class Panier(models.Model):
    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE)
    produits = models.ManyToManyField(Produit, through='ElementPanier')

    def __str__(self):
        return f"Panier de {self.utilisateur.username}"

class ElementPanier(models.Model):
    panier = models.ForeignKey(Panier, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Produit: {self.produit.libelle}, Quantité: {self.quantite}"
