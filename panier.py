TVA = 0.21

def calculer_total(prix, quantite):
    """
    Calcule le total du panier.
    p: prix unitaire
    q: quantité
    """
    return prix * quantite * (1 + TVA)
