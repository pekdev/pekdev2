from django.db import models
from django.contrib.auth.models import User

class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"
    
    def __str__(self):
        return self.nom

class Produit(models.Model):
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='produits')
    nom = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=0)
    image = models.ImageField(upload_to='produits/')
    stock = models.IntegerField(default=0)
    disponible = models.BooleanField(default=True)
    date_ajout = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Produit"
        verbose_name_plural = "Produits"
    
    def __str__(self):
        return self.nom

class Projet(models.Model):
    CATEGORIE_CHOICES = [
        ('web', 'Web'),
        ('app', 'Application'),
        ('design', 'Design'),
    ]
    
    titre = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)  # Ajoutez cette ligne
    description = models.TextField()
    categorie = models.CharField(max_length=20, choices=CATEGORIE_CHOICES)
    image = models.ImageField(upload_to='projets/', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    lien = models.URLField(blank=True, null=True)
    date_realisation = models.DateField()
    
    class Meta:
        verbose_name = "Projet"
        verbose_name_plural = "Projets"
    
    def __str__(self):
        return self.titre

class Article(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    image = models.ImageField(upload_to='blog/')
    date_publication = models.DateTimeField(auto_now_add=True)
    auteur = models.CharField(max_length=100, default="Elvis Mugisha")
    
    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        ordering = ['-date_publication']
    
    def __str__(self):
        return self.titre

class Temoignage(models.Model):
    auteur = models.CharField(max_length=200)
    fonction = models.CharField(max_length=200, blank=True)
    texte = models.TextField()
    photo = models.ImageField(upload_to='temoignages/', blank=True, null=True)
    date_ajout = models.DateTimeField(auto_now_add=True)
    actif = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Témoignage"
        verbose_name_plural = "Témoignages"
    
    def __str__(self):
        return self.auteur

class Contact(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    sujet = models.CharField(max_length=200)
    message = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)
    traite = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
        ordering = ['-date_envoi']
    
    def __str__(self):
        return f"{self.nom} - {self.sujet}"

class Commande(models.Model):
    STATUS_CHOICES = [
        ('en_attente', 'En attente'),
        ('confirmee', 'Confirmée'),
        ('expediee', 'Expédiée'),
        ('livree', 'Livrée'),
        ('annulee', 'Annulée'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
    adresse = models.TextField()
    total = models.DecimalField(max_digits=10, decimal_places=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='en_attente')
    date_commande = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Commande"
        verbose_name_plural = "Commandes"
        ordering = ['-date_commande']
    
    def __str__(self):
        return f"Commande #{self.id} - {self.nom}"

class LigneCommande(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE, related_name='lignes')
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.IntegerField()
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=0)
    
    def __str__(self):
        return f"{self.quantite} x {self.produit.nom}"