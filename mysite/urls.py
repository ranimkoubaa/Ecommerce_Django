"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


"""from django.contrib import admin
from django.urls import path,include
#from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('magasin/', include('magasin.urls'))
]"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
#from . import views
from django.conf.urls.static import static
from . import views
from django.contrib import admin, auth
from django.contrib.auth import views as auth_views

from django.urls import include, path
from rest_framework import routers
from magasin.views import ProductViewset ,CategoryAPIView
router = routers.SimpleRouter()
#router.register('produit', ProductViewset, basename='produit')
router.register(r'produit', ProductViewset, basename='produit')

urlpatterns = [
path('admin/', admin.site.urls),
path('', views.index, name='accueil'),
path('magasin/',include('magasin.urls')),
path('accounts/', include('django.contrib.auth.urls')),
path('login/',auth_views.LoginView.as_view(template_name='registration/login.html'), name = 'login'),
path('logout/',auth_views.LogoutView.as_view(template_name='registration/logout.html'), name ='logout'),
path('api-auth/', include('rest_framework.urls')),
path('api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

