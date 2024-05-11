from rest_framework.serializers import ModelSerializer
from magasin.models import Categorie
class CategorySerializer(ModelSerializer):
 class Meta:
    model = Categorie
    fields = ['id', 'categorie']
    
from rest_framework.serializers import ModelSerializer
from .models import Produit

class ProduitSerializer(ModelSerializer):
    class Meta:
        model = Produit
        fields = ['id', 'libelle', 'description', 'categorie' , 'prix' , 'img']
