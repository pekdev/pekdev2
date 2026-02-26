from django.contrib import admin
from .models import *

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ['nom', 'slug', 'date_creation']
    prepopulated_fields = {'slug': ('nom',)}
    search_fields = ['nom']

@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ['nom', 'categorie', 'prix', 'stock', 'disponible', 'date_ajout']
    list_filter = ['categorie', 'disponible']
    prepopulated_fields = {'slug': ('nom',)}
    search_fields = ['nom', 'description']
    list_editable = ['prix', 'stock', 'disponible']

@admin.register(Projet)
class ProjetAdmin(admin.ModelAdmin):
    list_display = ['titre', 'categorie', 'date_realisation']
    list_filter = ['categorie']
    # Supprimer ou corriger prepopulated_fields
    # prepopulated_fields = {'slug': ('titre',)}  # Commentez cette ligne
    search_fields = ['titre', 'description']

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['titre', 'auteur', 'date_publication']
    list_filter = ['auteur']
    search_fields = ['titre', 'contenu']
    date_hierarchy = 'date_publication'

@admin.register(Temoignage)
class TemoignageAdmin(admin.ModelAdmin):
    list_display = ['auteur', 'fonction', 'actif', 'date_ajout']
    list_filter = ['actif']
    list_editable = ['actif']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['nom', 'email', 'sujet', 'date_envoi', 'traite']
    list_filter = ['traite']
    list_editable = ['traite']
    search_fields = ['nom', 'email', 'sujet', 'message']
    readonly_fields = ['date_envoi']

class LigneCommandeInline(admin.TabularInline):
    model = LigneCommande
    extra = 0
    readonly_fields = ['produit', 'quantite', 'prix_unitaire']

@admin.register(Commande)
class CommandeAdmin(admin.ModelAdmin):
    list_display = ['id', 'nom', 'email', 'total', 'status', 'date_commande']
    list_filter = ['status']
    list_editable = ['status']
    search_fields = ['nom', 'email', 'telephone']
    readonly_fields = ['date_commande']
    inlines = [LigneCommandeInline]