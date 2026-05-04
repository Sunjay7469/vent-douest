from django.contrib import admin
from django.urls import path
from website.views import home # Importe ta vue

urlpatterns = [
    path('admin/', admin.site.set.urls),
    path('', home, name='home'), # L'adresse vide '' correspond à l'accueil
]
