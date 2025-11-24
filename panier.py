nombre_reduction = 50
valeur_reduction = 0.10

def calculer_total(prix, quantite):
    if quantite >= nombre_reduction:
        return prix * quantite * (1 - valeur_reduction)
    return prix * quantite