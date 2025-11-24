TVA = 0.21
nombre_reduction = 50
valeur_reduction = 0.10

def calculer_total(prix, quantite):
    """
    Calcule le total du panier.
    prix: prix unitaire
    quantite: quantité
    """
    montant_TVAC = prix * quantite * (1 + TVA)
    
    if quantite >= nombre_reduction:
        return montant_TVAC * (1 - valeur_reduction)
    return montant_TVAC
