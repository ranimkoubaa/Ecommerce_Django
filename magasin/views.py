from django.shortcuts import render , get_object_or_404

from django.template import loader
from .models import Produit
from .forms import ProduitForm
from django.shortcuts import redirect
#from django.http import  HttpResponseRedirect

from audioop import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .forms import FournisseurForm
from .models import Fournisseur
from .models import Commande
from .forms import CommandeForm

# Create your views here.


"""def index(request):
    #template=loader.get_template('magasin/mesProduits.html')
    products= Produit.objects.all()
    context={'products':products}
    return render(request,'magasin/mesProduits.html',context)"""

def index(request):
    #template=loader.get_template('magasin/mesProduits.html')
      list=Produit.objects.all()
      return render(request,'magasin/home.html',{'list':list})

def indajout(request):
 if request.method == "POST" :
    form = ProduitForm(request.POST,request.FILES)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/magasin')
 else :
    form = ProduitForm() #créer formulaire vide
    return render(request,'magasin/majProduits.html',{'form':form})

from django.shortcuts import render
from .models import Fournisseur

def liste_fournisseurs(request):
    query = request.GET.get('q')
    fournisseurs = Fournisseur.objects.all()

    if query:
        fournisseurs = fournisseurs.filter(nom__icontains=query)

    return render(request, 'magasin/ListFournisseur.html', {'fournisseurs': fournisseurs, 'query': query})

"""def liste_fournisseurs(request):
    fournisseurs = Fournisseur.objects.all()
    return render(request, 'magasin/ListFournisseur.html', {'fournisseurs': fournisseurs})"""

def nouveauFournisseur(request):
    if request.method == 'POST':
        form = FournisseurForm(request.POST)
        if form.is_valid():
            form.save()
            # Récupérer à nouveau la liste des fournisseurs après l'ajout
            fournisseurs = Fournisseur.objects.all()
            return render(request, 'magasin/ListFournisseur.html', {'fournisseurs': fournisseurs})
    else:
        form = FournisseurForm()
    return render(request, 'magasin/AjoutFournisseur.html', {'form': form})



from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

def delete_Fournisseur(request, fk):
    try:
        fournisseur = Fournisseur.objects.get(id=fk)
    except Fournisseur.DoesNotExist:
        # Gérer le cas où le fournisseur n'existe pas
        return redirect('ListFournisseur')  # Redirection vers la liste des fournisseurs

    if request.method == 'POST':
        fournisseur.delete()
        return redirect('ListFournisseur')  # Redirection vers la liste des fournisseurs

    return render(request, 'magasin/delete_For.html', {'fournisseur': fournisseur})



from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Fournisseur
from .forms import FournisseurForm

def edit_Fournisseur(request, fk):
    fournisseur = get_object_or_404(Fournisseur, id=fk)
    
    if request.method == 'POST':
        form = FournisseurForm(request.POST, request.FILES, instance=fournisseur)
        if form.is_valid():
            frns = form.save(commit=False)
            nouvelle_image = form.cleaned_data.get('logo', None)
            if nouvelle_image:
                frns.logo = nouvelle_image
            frns.save()
            return redirect('ListFournisseur') 
    else:
        form = FournisseurForm(instance=fournisseur)
    
    return render(request, 'magasin/edit_For.html', {'form': form})



def detail_Fournisseur(request, for_id):
    fournisseur = get_object_or_404(Fournisseur, id=for_id)
    context = {'fournisseur': fournisseur}
    return render(request, 'magasin/detail_For.html', context)


# magasin/views.py

from django.shortcuts import render
from django.views.generic import ListView
from .models import Commande

class ListeCommandesView(ListView):
    model = Commande
    template_name = 'magasin/liste_commandes.html'
    context_object_name = 'commandes'

    def get_queryset(self):
        return Commande.objects.all()
    
from .forms import CommandeForm

"""def ajouter_commande(request):
    if request.method == 'POST':
        form = CommandeForm(request.POST)
        if form.is_valid():
            produits_ids = request.POST.getlist('produits')
            totalCde = sum(Produit.objects.filter(id__in=produits_ids).values_list('prix', flat=True))
            form.totalCde=totalCde
            form.save()
            return redirect('liste_commandes')  # Rediriger vers la liste des commandes après l'ajout
    else:
        form = CommandeForm()
    return render(request, 'magasin/ajouter_commande.html', {'form': form})
"""
from django.shortcuts import render, redirect
from .models import Commande
from .forms import CommandeForm
from magasin.models import Produit

def ajouter_commande(request):
    if request.method == 'POST':
        form = CommandeForm(request.POST)
        if form.is_valid():
            produits_ids = request.POST.getlist('produits')
            totalCde = sum(Produit.objects.filter(id__in=produits_ids).values_list('prix', flat=True))

            # Créer une instance de Commande à partir des données du formulaire
            nouvelle_commande = form.save(commit=False)
            nouvelle_commande.totalCde = totalCde  # Définir le champ totalCde avec le calcul du total
            nouvelle_commande.save()

            return redirect('liste_commandes')  # Rediriger vers la liste des commandes après l'ajout
    else:
        form = CommandeForm()
    
    return render(request, 'magasin/ajouter_commande.html', {'form': form})


from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
class SupprimerCommandeView(DeleteView):
    model = Commande
    template_name = 'magasin/supprimer_commande.html'
    success_url = reverse_lazy('liste_commandes')

def modifier_commande(request, pk):
    commande = get_object_or_404(Commande, pk=pk)

    if request.method == 'POST':
        form = CommandeForm(request.POST, instance=commande)
        if form.is_valid():
            form.save()
            return redirect('liste_commandes')
    else:
        form = CommandeForm(instance=commande)

    return render(request, 'magasin/modifier_commande.html', {'form': form, 'commande': commande})
def detail_commande(request, pk):
    commande = get_object_or_404(Commande, pk=pk)
    return render(request, 'magasin/detail_commande.html', {'commande': commande})


from django.contrib.auth.views import LoginView

"""class CustomLoginView(LoginView):
    template_name = 'registration/login.html'  # Définissez le chemin vers votre template de login personnalisé si nécessaire
""" 



from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        # Définir l'URL de redirection après connexion réussie
        return redirect('acceuil')  # Remplacez 'votre_nom_url' par le nom de la vue ou l'URL de redirection souhaitée

    def form_valid(self, form):
        # Gérer la connexion réussie ici
        return HttpResponseRedirect(self.get_success_url())



from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect

def custom_logout(request):
    return render(request, 'registration/logout.html')

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')  # Redirection vers la page de connexion après déconnexion



from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

# Dans views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(
                request, f'Bonjour {username}, Votre compte a été créé avec succès !')
            return render(request, 'registration/login.html')  # Rendu de la page de connexion
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


from django.contrib.auth.mixins import LoginRequiredMixin    
from django.contrib.auth.views import PasswordChangeView as DjangoPasswordChangeView    
from django.urls import reverse_lazy
from django.contrib.auth.forms import PasswordChangeForm
from django.views.generic import FormView

class CustomPasswordChangeView(LoginRequiredMixin, DjangoPasswordChangeView):
    template_name = 'registration/password_change_form.html'  # Chemin vers votre modèle de formulaire personnalisé
    success_url = reverse_lazy('password_change_done')  # Rediriger vers l'URL de réussite après le changement de mot de passe
    form_class = PasswordChangeForm  # Utiliser le formulaire de changement de mot de passe par défaut

    def form_valid(self, form):
        # Logique supplémentaire si nécessaire avant de valider le formulaire
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Ajouter des données contextuelles supplémentaires si nécessaire
        return context
from django.views.generic import TemplateView

class PasswordChangeDoneView(TemplateView):
    template_name = 'magasin/password_change_done.html'
    
    
from django.views.generic import TemplateView
class PasswordResetView(TemplateView):
    template_name = 'magasin/password_reset.html'
    # Ajoutez d'autres logiques nécessaires pour la vue de réinitialisation du mot de passe
    
from django.views.generic import TemplateView

class PasswordResetDoneView(TemplateView):
    template_name = 'magasin/password_reset_done.html'
    # Ajoutez d'autres logiques nécessaires pour la vue de réinitialisation du mot de passe réussie
from django.views.generic import TemplateView

class PasswordResetDoneView(TemplateView):
    template_name = 'magasin/password_reset_done.html'
    # Ajoutez d'autres logiques nécessaires pour la vue de réinitialisation du mot de passe réussie

class PasswordResetConfirmView(TemplateView):
    template_name = 'magasin/password_reset_confirm.html'
    # Ajoutez d'autres logiques nécessaires pour la vue de confirmation de réinitialisation du mot de passe
from django.views.generic import TemplateView

class PasswordResetCompleteView(TemplateView):
    template_name = 'magasin/password_reset_complete.html'
    # Ajoutez d'autres logiques nécessaires pour la vue de réinitialisation du mot de passe complétée



f"""rom django.shortcuts import render

def home(request):
    # Logique de la vue home
    return render(request, 'magasin/home.html')  # Renvoie le rendu du template 'magasin/home.html'"""
from django.shortcuts import render
from .models import Produit

def home(request):
    produits = Produit.objects.all()  # Récupérer tous les produits depuis la base de données
    return render(request, 'magasin/home.html', {'produits': produits})

from django.shortcuts import render, get_object_or_404
from .models import Produit
from django.shortcuts import redirect, get_object_or_404
from .models import Produit

"""def ajouter_panier(request, produit_id):
    produit = get_object_or_404(Produit, pk=produit_id)
    if 'panier' not in request.session:
        request.session['panier'] = []  # Initialiser le panier s'il n'existe pas encore
    request.session['panier'].append(produit_id)  # Ajouter l'identifiant du produit au panier
    return redirect('panier')  # Rediriger vers la page du panier

def panier(request):
    panier_produits = []
    if 'panier' in request.session:
        panier_produits = Produit.objects.filter(id__in=request.session['panier'])
    return render(request, 'magasin/panier.html', {'panier_produits': panier_produits})"""
    
# views.py dans votre application magasin
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Produit, Panier, ElementPanier

@login_required
def ajouter_panier(request, produit_id):
    produit = Produit.objects.get(id=produit_id)
    panier, created = Panier.objects.get_or_create(utilisateur=request.user)
    element_panier, created = ElementPanier.objects.get_or_create(panier=panier, produit=produit)
    element_panier.quantite += 1
    element_panier.save()

    # Récupérer tous les éléments du panier pour l'afficher dans le template
    elements_panier = ElementPanier.objects.filter(panier=panier)
    total = sum(element.produit.prix * element.quantite for element in elements_panier)

    # Passer les éléments du panier et le total au template
    context = {
        'elements_panier': elements_panier,
        'total': total,
    }

    # Rendre le template associé au panier avec le contexte
    return render(request, 'magasin/panier.html', context)

@login_required
def panier(request):
    panier = Panier.objects.get(utilisateur=request.user)
    elements_panier = ElementPanier.objects.filter(panier=panier)

    # Calculer le total en parcourant tous les éléments du panier
    total = sum(element.produit.prix * element.quantite for element in elements_panier)

    # Passer les éléments du panier et le total au template
    context = {
        'elements_panier': elements_panier,
        'total': total,
    }

    return render(request, 'magasin/panier.html', context)

from django.shortcuts import render

from django.shortcuts import render

def paiement(request):
    context = {
        'message': 'Votre paiement a été effectué avec succès.'
    }
    messages.success(request, "Paiement effectué avec succès ! Merci pour votre commande.")
    return render(request, 'magasin/paiement.html', context)
from django.shortcuts import render

from django.shortcuts import redirect, get_object_or_404
from .models import ElementPanier

def supprimer_produit_panier(request, element_id):
    element_panier = get_object_or_404(ElementPanier, id=element_id)
    element_panier.delete()
    return redirect('panier')  # Redirige vers la page du panier après suppression
from django.shortcuts import render

from django.shortcuts import render
from .models import ElementPanier

def process_paiement(request):
    panier = request.session.get('panier')  # Assurez-vous de récupérer le panier correctement depuis la session
    elements_panier = ElementPanier.objects.filter(panier=panier)

    total = sum(element.produit.prix * element.quantite for element in elements_panier)

    context = {
        'elements_panier': elements_panier,
        'total': total,
    }
    

    return render(request, 'magasin/process_paiement.html', context)


from rest_framework.views import APIView
from rest_framework.response import Response
from magasin.models import Categorie
from magasin.serializers import CategorySerializer
class CategoryAPIView(APIView):
     def get(self, *args, **kwargs):
        categories = Categorie.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from .models import Produit
from .serializers import ProduitSerializer  # Make sure to import correctly

class ProduitAPIView(APIView):
    serializer_class = ProduitSerializer
    def get(self, request, *args, **kwargs):
        produits = Produit.objects.all()
        serializer = ProduitSerializer(produits, many=True)
        return Response(serializer.data)
    
from rest_framework import viewsets
from .models import Produit
from .serializers import ProduitSerializer

class ProductViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProduitSerializer

    def get_queryset(self):
        queryset = Produit.objects.all()
        product_id = self.kwargs.get('pk')
        
        if product_id:
            queryset = queryset.filter(id=product_id)
        
        return queryset
    
    
    















