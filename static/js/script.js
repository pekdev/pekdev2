
// Données des produits
const produits = [
  {
    id: 1,
    nom: "iPhone 13 Pro",
    description: "Dernier smartphone Apple avec écran Super Retina XDR et processeur A15 Bionic.",
    prix: 999,
    image: "https://source.unsplash.com/random/300x300/?iphone",
    categorie: "telephone"
  },
  {
    id: 2,
    nom: "Samsung Galaxy S22",
    description: "Smartphone Android haut de gamme avec appareil photo professionnel.",
    prix: 849000,
    image: "s22.jpeg",
    categorie: "telephone"
  },
  {
    id: 3,
    nom: "MacBook Pro 14\"",
    description: "Ordinateur portable puissant avec puce M1 Pro pour les professionnels.",
    prix: 1999,
    image: "https://source.unsplash.com/random/300x300/?macbook",
    categorie: "ordinateur"
  },
  {
    id: 4,
    nom: "Dell XPS 13",
    description: "PC portable ultra-fin avec écran InfinityEdge et processeur Intel Core i7.",
    prix: 1299,
    image: "https://source.unsplash.com/random/300x300/?laptop",
    categorie: "ordinateur"
  },
  {
    id: 5,
    nom: "Casque Sony WH-1000XM4",
    description: "Casque sans fil avec annulation de bruit exceptionnelle et autonomie de 30h.",
    prix: 349,
    image: "https://source.unsplash.com/random/300x300/?headphones",
    categorie: "accessoire"
  },
  {
    id: 6,
    nom: "Souris Logitech MX Master 3",
    description: "Souris sans fil ergonomique pour une productivité maximale.",
    prix: 99,
    image: "https://source.unsplash.com/random/300x300/?mouse",
    categorie: "accessoire"
  },
  {
    id: 7,
    nom: "Huawei P50 Pro",
    description: "Smartphone avec un appareil photo Leica exceptionnel et design élégant.",
    prix: 899,
    image: "https://source.unsplash.com/random/300x300/?huawei",
    categorie: "telephone"
  },
  {
    id: 8,
    nom: "iPad Pro 12.9\"",
    description: "Tablette polyvalente avec puce M1 et écran Liquid Retina XDR.",
    prix: 1099,
    image: "https://source.unsplash.com/random/300x300/?ipad",
    categorie: "ordinateur"
  }
];

// Panier
let panier = [];
const panierIcon = document.getElementById('panier-icon');
const panierSidebar = document.getElementById('panier-sidebar');
const fermerPanier = document.getElementById('fermer-panier');
const panierItems = document.getElementById('panier-items');
const panierTotal = document.getElementById('panier-total');
const panierCount = document.getElementById('panier-count');
const passerCommande = document.getElementById('passer-commande');

// Menu responsive
const toggle = document.getElementById("menu-toggle");
const navbar = document.getElementById("navbar");
toggle.addEventListener("click", () => {
  navbar.classList.toggle("active");
  toggle.classList.toggle("active");
});

// Fermer le menu en cliquant sur un lien
document.querySelectorAll("nav a").forEach(link => {
  link.addEventListener("click", () => {
    navbar.classList.remove("active");
    toggle.classList.remove("active");
  });
});

// Animation au défilement
const sections = document.querySelectorAll(".section");
const showOnScroll = () => {
  const trigger = window.innerHeight / 1.2;
  sections.forEach(sec => {
    const top = sec.getBoundingClientRect().top;
    if (top < trigger) sec.classList.add("visible");
  });
};
window.addEventListener("scroll", showOnScroll);
showOnScroll();

// Animation des compétences
const skills = document.querySelectorAll(".progress-bar");
window.addEventListener("scroll", () => {
  skills.forEach(bar => {
    const pos = bar.getBoundingClientRect().top;
    if (pos < window.innerHeight - 50) {
      bar.style.width = bar.getAttribute("data-skill") + "%";
    }
  });
});

// Filtrage du portfolio
const filterButtons = document.querySelectorAll(".filter-btn");
const portfolioItems = document.querySelectorAll(".portfolio-item");

filterButtons.forEach(button => {
  button.addEventListener("click", () => {
    // Retirer la classe active de tous les boutons
    filterButtons.forEach(btn => btn.classList.remove("active"));
    // Ajouter la classe active au bouton cliqué
    button.classList.add("active");
    
    const filter = button.getAttribute("data-filter");
    
    portfolioItems.forEach(item => {
      if (filter === "all" || item.getAttribute("data-category") === filter) {
        item.style.display = "block";
      } else {
        item.style.display = "none";
      }
    });
  });
});

// Modal pour portfolio et blog
const modal = document.getElementById("modal");
const modalTitle = document.getElementById("modal-title");
const modalText = document.getElementById("modal-text");
const closeModal = document.getElementById("close");

document.querySelectorAll(".portfolio-item, .blog-card").forEach(el => {
  el.addEventListener("click", () => {
    if (el.classList.contains("portfolio-item")) {
      modalTitle.textContent = el.querySelector("h3").textContent;
      modalText.textContent = el.querySelector("p").textContent;
    } else {
      modalTitle.textContent = el.querySelector("h3").textContent;
      modalText.textContent = el.querySelector("p").textContent;
    }
    modal.style.display = "flex";
    document.body.style.overflow = "hidden";
  });
});

closeModal.addEventListener("click", () => {
  modal.style.display = "none";
  document.body.style.overflow = "auto";
});

window.addEventListener("click", (e) => {
  if (e.target === modal) {
    modal.style.display = "none";
    document.body.style.overflow = "auto";
  }
});

// Mode sombre
const modeBtn = document.getElementById("mode-btn");
modeBtn.addEventListener("click", () => {
  document.body.classList.toggle("dark-mode");
  if (document.body.classList.contains("dark-mode")) {
    modeBtn.innerHTML = '<i class="fas fa-sun"></i>';
    localStorage.setItem("theme", "dark");
  } else {
    modeBtn.innerHTML = '<i class="fas fa-moon"></i>';
    localStorage.setItem("theme", "light");
  }
});

// Charger le thème sauvegardé
if (localStorage.getItem("theme") === "dark") {
  document.body.classList.add("dark-mode");
  modeBtn.innerHTML = '<i class="fas fa-sun"></i>';
}

// Formulaire de contact
const contactForm = document.getElementById("contact-form");
contactForm.addEventListener("submit", (e) => {
  e.preventDefault();
  
  // Récupération des valeurs du formulaire
  const name = document.getElementById("name").value;
  const email = document.getElementById("email").value;
  const subject = document.getElementById("subject").value;
  const message = document.getElementById("message").value;
  
  // Ici, vous pouvez ajouter le code pour envoyer le formulaire
  // Par exemple, utiliser EmailJS, Formspree ou une requête AJAX
  
  // Simulation d'envoi réussi
  alert(`Merci ${name} ! Votre message a été envoyé avec succès.`);
  contactForm.reset();
});

// Bouton back to top
const backToTopBtn = document.getElementById("back-to-top");
window.addEventListener("scroll", () => {
  if (window.pageYOffset > 300) {
    backToTopBtn.classList.add("visible");
  } else {
    backToTopBtn.classList.remove("visible");
  }
});

backToTopBtn.addEventListener("click", () => {
  window.scrollTo({
    top: 0,
    behavior: "smooth"
  });
});

// Fonction pour faire défiler jusqu'à une section
function scrollToSection(sectionId) {
  document.getElementById(sectionId).scrollIntoView({
    behavior: "smooth"
  });
}

// Afficher les produits dans la boutique
function afficherProduits() {
  const boutiqueGrid = document.getElementById('boutique-grid');
  boutiqueGrid.innerHTML = '';
  
  produits.forEach(produit => {
    const produitCard = document.createElement('div');
    produitCard.className = 'produit-card';
    produitCard.dataset.categorie = produit.categorie;
    
    produitCard.innerHTML = `
      <img src="${produit.image}" alt="${produit.nom}" class="produit-image">
      <div class="produit-info">
        <h3 class="produit-titre">${produit.nom}</h3>
        <p class="produit-description">${produit.description}</p>
        <div class="produit-prix">${produit.prix} Fbu</div>
        <button class="ajouter-panier" data-id="${produit.id}">Ajouter au panier</button>
      </div>
    `;
    
    boutiqueGrid.appendChild(produitCard);
  });
  
  // Ajouter les événements aux boutons "Ajouter au panier"
  document.querySelectorAll('.ajouter-panier').forEach(btn => {
    btn.addEventListener('click', (e) => {
      const id = parseInt(e.target.dataset.id);
      ajouterAuPanier(id);
    });
  });
}

// Ajouter un produit au panier
function ajouterAuPanier(id) {
  const produit = produits.find(p => p.id === id);
  const existingItem = panier.find(item => item.id === id);
  
  if (existingItem) {
    existingItem.quantite += 1;
  } else {
    panier.push({...produit, quantite: 1});
  }
  
  mettreAJourPanier();
  ouvrirPanier();
}

// Mettre à jour l'affichage du panier
function mettreAJourPanier() {
  panierItems.innerHTML = '';
  
  if (panier.length === 0) {
    panierItems.innerHTML = '<div class="panier-vide">Votre panier est vide</div>';
    panierTotal.textContent = 'Total: 0 Fbu';
    panierCount.textContent = '0';
    return;
  }
  
  let total = 0;
  let count = 0;
  
  panier.forEach(item => {
    const itemTotal = item.prix * item.quantite;
    total += itemTotal;
    count += item.quantite;
    
    const panierItem = document.createElement('div');
    panierItem.className = 'panier-item';
    panierItem.innerHTML = `
      <img src="${item.image}" alt="${item.nom}" class="panier-item-image">
      <div class="panier-item-details">
        <div class="panier-item-nom">${item.nom}</div>
        <div class="panier-item-prix">${item.prix} Fbu x ${item.quantite} = ${itemTotal} Fbu</div>
        <div class="panier-quantite">
          <button class="quantite-btn moins" data-id="${item.id}">-</button>
          <span class="quantite">${item.quantite}</span>
          <button class="quantite-btn plus" data-id="${item.id}">+</button>
          <button class="supprimer-item" data-id="${item.id}"><i class="fas fa-trash"></i></button>
        </div>
      </div>
    `;
    
    panierItems.appendChild(panierItem);
  });
  
  panierTotal.textContent = `Total: ${total} Fbu`;
  panierCount.textContent = count;
  
  // Ajouter les événements aux boutons de quantité
  document.querySelectorAll('.quantite-btn.moins').forEach(btn => {
    btn.addEventListener('click', (e) => {
      const id = parseInt(e.target.dataset.id);
      modifierQuantite(id, -1);
    });
  });
  
  document.querySelectorAll('.quantite-btn.plus').forEach(btn => {
    btn.addEventListener('click', (e) => {
      const id = parseInt(e.target.dataset.id);
      modifierQuantite(id, 1);
    });
  });
  
  document.querySelectorAll('.supprimer-item').forEach(btn => {
    btn.addEventListener('click', (e) => {
      const id = parseInt(e.target.closest('.supprimer-item').dataset.id);
      supprimerDuPanier(id);
    });
  });
}

// Modifier la quantité d'un produit dans le panier
function modifierQuantite(id, changement) {
  const item = panier.find(item => item.id === id);
  
  if (item) {
    item.quantite += changement;
    
    if (item.quantite <= 0) {
      supprimerDuPanier(id);
    } else {
      mettreAJourPanier();
    }
  }
}

// Supprimer un produit du panier
function supprimerDuPanier(id) {
  panier = panier.filter(item => item.id !== id);
  mettreAJourPanier();
}

// Ouvrir le panier
function ouvrirPanier() {
  panierSidebar.classList.add('open');
  document.body.style.overflow = 'hidden';
}

// Fermer le panier
function fermerPanierHandler() {
  panierSidebar.classList.remove('open');
  document.body.style.overflow = 'auto';
}

// Passer commande
function passerCommandeHandler() {
  if (panier.length === 0) {
    alert('Votre panier est vide. Ajoutez des produits avant de passer commande.');
    return;
  }
  
  const total = panier.reduce((sum, item) => sum + (item.prix * item.quantite), 0);
  
  alert(`Commande passée avec succès ! Total: ${total} Fbu. Merci pour votre achat.`);
  
  // Vider le panier après la commande
  panier = [];
  mettreAJourPanier();
  fermerPanierHandler();
}

// Filtrer les produits de la boutique
function filtrerProduits() {
  const boutiquesFilterButtons = document.querySelectorAll('#boutique .filter-btn');
  const produitsCards = document.querySelectorAll('.produit-card');
  
  boutiquesFilterButtons.forEach(button => {
    button.addEventListener('click', () => {
      // Retirer la classe active de tous les boutons
      boutiquesFilterButtons.forEach(btn => btn.classList.remove('active'));
      // Ajouter la classe active au bouton cliqué
      button.classList.add('active');
      
      const filter = button.getAttribute('data-filter');
      
      produitsCards.forEach(card => {
        if (filter === 'all' || card.getAttribute('data-categorie') === filter) {
          card.style.display = 'block';
        } else {
          card.style.display = 'none';
        }
      });
    });
  });
}

// Initialisation
document.addEventListener('DOMContentLoaded', () => {
  afficherProduits();
  mettreAJourPanier();
  filtrerProduits();
  
  // Événements pour le panier
  panierIcon.addEventListener('click', ouvrirPanier);
  fermerPanier.addEventListener('click', fermerPanierHandler);
  passerCommande.addEventListener('click', passerCommandeHandler);
});

