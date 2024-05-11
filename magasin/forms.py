from django.forms import ModelForm
from .models import Produit
from .models import Fournisseur
from .models import Categorie
from .models import Commande
from django import forms
class ProduitForm(ModelForm):
    class Meta :
        model = Produit
        fields = "__all__" #pour tous les champs de la table
        #fields=['libelle','description'] #pour qulques champs
class FournisseurForm(ModelForm):
    class Meta:
        model = Fournisseur 
        fields = "__all__"

class CategorieForm(ModelForm):
    class Meta:
        model = Categorie
        fields = ['categorie']

class CommandeForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = ['numero_commande', 'dateCde', 'produits']
        widgets = {
            'produits': forms.CheckboxSelectMultiple()
        }
        
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
"""class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='Prénom')
    last_name = forms.CharField(label='Nom')
    email = forms.EmailField(label='Adresse e-mail')
class Meta(UserCreationForm.Meta):
    model = User
    fields = UserCreationForm.Meta.fields + ('first_name', 'last_name' , 'email')
""" 
"""class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']"""
        
        
"""class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='Prénom')
    last_name = forms.CharField(label='Nom')
    email = forms.EmailField(label='Adresse e-mail')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + \
            ('first_name', 'last_name', 'email')"""
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class UserRegistrationForm(UserCreationForm):
 first_name = forms.CharField(label='Prénom')
 last_name = forms.CharField(label='Nom')
 email = forms.EmailField(label='Adresse e-mail')

class Meta(UserCreationForm.Meta):
 model = User
 fields = UserCreationForm.Meta.fields + ('first_name', 'last_name' , 'email')
 
 


