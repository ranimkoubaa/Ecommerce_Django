from django.shortcuts import render
from django.template import loader
from django.contrib.auth.decorators import login_required
@login_required
def index(request):
    """return render(request,'acceuil.html' )"""
    context={'val':"Menu Acceuil"}
    return render(request,'accueil.html',context)
