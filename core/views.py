from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json
from .models import *

def index(request):
    """Page d'accueil"""
    projets = Projet.objects.all()[:3]
    produits = Produit.objects.filter(disponible=True)[:4]
    articles = Article.objects.all()[:3]
    temoignages = Temoignage.objects.filter(actif=True)
    
    context = {
        'projets': projets,
        'produits': produits,
        'articles': articles,
        'temoignages': temoignages,
    }
    return render(request, 'core/index.html', context)

def projets(request):
    """Liste des projets"""
    projets_list = Projet.objects.all()
    categories = Projet.CATEGORIE_CHOICES
    
    context = {
        'projets': projets_list,
        'categories': categories,
    }
    return render(request, 'core/projets.html', context)

def projet_detail(request, slug):
    """Détail d'un projet"""
    projet = get_object_or_404(Projet, slug=slug)
    return render(request, 'core/projet_detail.html', {'projet': projet})

def boutique(request):
    """Page de la boutique"""
    categorie_id = request.GET.get('categorie')
    if categorie_id:
        produits = Produit.objects.filter(categorie_id=categorie_id, disponible=True)
    else:
        produits = Produit.objects.filter(disponible=True)
    
    categories = Categorie.objects.all()
    
    context = {
        'produits': produits,
        'categories': categories,
    }
    return render(request, 'core/boutique.html', context)

def produit_detail(request, slug):
    """Détail d'un produit"""
    produit = get_object_or_404(Produit, slug=slug, disponible=True)
    return render(request, 'core/produit_detail.html', {'produit': produit})

def blog(request):
    """Page du blog"""
    articles = Article.objects.all()
    return render(request, 'core/blog.html', {'articles': articles})

def article_detail(request, id):
    """Détail d'un article"""
    article = get_object_or_404(Article, id=id)
    return render(request, 'core/article_detail.html', {'article': article})

def contact(request):
    """Page de contact"""
    if request.method == 'POST':
        nom = request.POST.get('name')
        email = request.POST.get('email')
        sujet = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Sauvegarder dans la base de données
        contact = Contact.objects.create(
            nom=nom,
            email=email,
            sujet=sujet,
            message=message
        )
        
        # Envoyer un email (optionnel)
        try:
            send_mail(
                f"Portfolio - {sujet}",
                f"De: {nom} ({email})\n\n{message}",
                settings.DEFAULT_FROM_EMAIL,
                ['votre-email@gmail.com'],
                fail_silently=True,
            )
        except:
            pass
        
        messages.success(request, "Votre message a été envoyé avec succès !")
        return redirect('contact')
    
    return render(request, 'core/contact.html')

def ajouter_panier(request, produit_id):
    """Ajouter un produit au panier"""
    if request.method == 'POST':
        produit = get_object_or_404(Produit, id=produit_id)
        quantite = int(request.POST.get('quantite', 1))
        
        panier = request.session.get('panier', {})
        
        if str(produit_id) in panier:
            panier[str(produit_id)] += quantite
        else:
            panier[str(produit_id)] = quantite
        
        request.session['panier'] = panier
        
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': True,
                'panier_count': sum(panier.values()),
                'message': f"{produit.nom} ajouté au panier"
            })
        
        messages.success(request, f"{produit.nom} ajouté au panier")
        return redirect('boutique')
    
    return redirect('boutique')

def panier(request):
    """Voir le panier"""
    panier_data = request.session.get('panier', {})
    produits = []
    total = 0
    
    for produit_id, quantite in panier_data.items():
        try:
            produit = Produit.objects.get(id=produit_id)
            sous_total = produit.prix * quantite
            produits.append({
                'produit': produit,
                'quantite': quantite,
                'sous_total': sous_total
            })
            total += sous_total
        except Produit.DoesNotExist:
            continue
    
    context = {
        'produits': produits,
        'total': total,
    }
    return render(request, 'core/panier.html', context)

def supprimer_panier(request, produit_id):
    """Supprimer un produit du panier"""
    if request.method == 'POST':
        panier = request.session.get('panier', {})
        
        if str(produit_id) in panier:
            del panier[str(produit_id)]
            request.session['panier'] = panier
            
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': True,
                    'panier_count': sum(panier.values()),
                    'message': "Produit supprimé du panier"
                })
        
        messages.success(request, "Produit supprimé du panier")
        return redirect('panier')
    
    return redirect('panier')

def commander(request):
    """Passer une commande"""
    if request.method == 'POST':
        panier_data = request.session.get('panier', {})
        
        if not panier_data:
            messages.error(request, "Votre panier est vide")
            return redirect('boutique')
        
        # Créer la commande
        commande = Commande.objects.create(
            user=request.user if request.user.is_authenticated else None,
            nom=request.POST.get('nom'),
            email=request.POST.get('email'),
            telephone=request.POST.get('telephone'),
            adresse=request.POST.get('adresse'),
            total=0  # Sera calculé après
        )
        
        total_commande = 0
        
        # Ajouter les lignes de commande
        for produit_id, quantite in panier_data.items():
            produit = Produit.objects.get(id=produit_id)
            LigneCommande.objects.create(
                commande=commande,
                produit=produit,
                quantite=quantite,
                prix_unitaire=produit.prix
            )
            total_commande += produit.prix * quantite
        
        commande.total = total_commande
        commande.save()
        
        # Vider le panier
        request.session['panier'] = {}
        
        messages.success(request, "Commande passée avec succès !")
        return redirect('commande_success', commande_id=commande.id)
    
    return render(request, 'core/commande.html')

def commande_success(request, commande_id):
    """Page de succès de commande"""
    commande = get_object_or_404(Commande, id=commande_id)
    return render(request, 'core/commande_success.html', {'commande': commande})