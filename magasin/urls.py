from django.urls import path   #,include

from . import views
from .views import ListeCommandesView , ajouter_commande ,  SupprimerCommandeView , modifier_commande , detail_commande
from django.contrib.auth import views as auth_views
from .views import CustomPasswordChangeView
from django.contrib.auth import views as auth_views
from .views import CustomLogoutView, custom_logout
from django.contrib.auth.views import LogoutView
from .views import CustomLogoutView, custom_logout

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from django.urls import path   
from . import views
from .views import CategoryAPIView, ProduitAPIView



urlpatterns = [
    
    path('', views.index, name='index'),
    path('magasin/majProduits.html', views.indajout, name='indajout'),
    path('AjoutFournisseur/', views.nouveauFournisseur, name='AjoutFournisseur'),
    path('ListFournisseur/', views.liste_fournisseurs, name='ListFournisseur'),
    # Autres URL...
    path('commandes/', ListeCommandesView.as_view(), name='liste_commandes'),
    path('ajouter_commande/', ajouter_commande, name='ajouter_commande'),
    path('commande/<int:pk>/supprimer/', SupprimerCommandeView.as_view(), name='supprimer_commande'),
    path('commande/<int:pk>/modifier/', modifier_commande, name='modifier_commande'),
    path('commande/<int:pk>/', detail_commande, name='detail_commande'),
    
    
     path ('deleteFournisseur/<int:fk>/', views.delete_Fournisseur, name='delete_Fournisseur'),
     path('editFournisseur/<int:fk>/', views.edit_Fournisseur, name='edit_Fournisseur'),
      path('Fournisseur/<int:for_id>/', views.detail_Fournisseur, name='detail_Fournisseur'),
      
      
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('custom-logout/', custom_logout, name='custom_logout'),
    
    #path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    
   path('register/',views.register, name = 'register'), 
   
    #path('login/', views.LoginView.as_view(), name='login'),
    #path('logout/', views.LogoutView.as_view(), name='logout'),
    #path('password_change/', views.PasswordChangeView.as_view(),name='password_change'),
    path('password_change/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', views.PasswordChangeDoneView.as_view(),name='password_change_done'),
    path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('magasin/home/', views.home, name='home'),  # Ajout de la nouvelle URL pour la vue home
     #path('ajouter_panier/<int:produit_id>/', views.ajouter_panier, name='ajouter_panier'),
     #path('panier/', views.panier, name='panier'),
    path('ajouter_panier/<int:produit_id>/', views.ajouter_panier, name='ajouter_panier'),
    path('panier/', views.panier, name='panier'),
    path('paiement/', views.paiement, name='paiement'),
    path('process_paiement/', views.process_paiement, name='process_paiement'),
    path('supprimer_produit_panier/<int:element_id>/', views.supprimer_produit_panier, name='supprimer_produit_panier'),
    path('api/category/', CategoryAPIView.as_view()),
    path('api/produits/', ProduitAPIView.as_view()),

]








