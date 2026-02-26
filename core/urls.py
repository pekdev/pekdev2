from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('projets/', views.projets, name='projets'),
    path('projet/<slug:slug>/', views.projet_detail, name='projet_detail'),
    path('boutique/', views.boutique, name='boutique'),
    path('produit/<slug:slug>/', views.produit_detail, name='produit_detail'),
    path('blog/', views.blog, name='blog'),
    path('article/<int:id>/', views.article_detail, name='article_detail'),
    path('contact/', views.contact, name='contact'),
    path('ajouter-panier/<int:produit_id>/', views.ajouter_panier, name='ajouter_panier'),
    path('panier/', views.panier, name='panier'),
    path('supprimer-panier/<int:produit_id>/', views.supprimer_panier, name='supprimer_panier'),
    path('commander/', views.commander, name='commander'),
    path('commande/success/', views.commande_success, name='commande_success'),
]