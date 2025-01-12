import random
#Fonction qui génère une combinaison sécrètede couleur

def generate_combination(taille=4):
    # Liste des couleurs acceptées
    color_accepted = ['vert', 'rouge', 'jaune', 'orange', 'blanc', 'violet']

    # Génère une combinaison aléatoire de la taille spécifiée
    alea = [random.choice(color_accepted) for _ in range(taille)]
    
    return alea

def player_proposition():
    # Demander une proposition de combinaison de couleurs
    proposition = input("Entrez votre proposition de combinaison (séparée par des espaces) : ")
    
    # Séparer les couleurs par espace et valider la longueur de la combinaison
    proposition_list = proposition.split()
    
    # Vérifier si le nombre de couleurs correspond à la taille attendue (par exemple, 4)
    taille_combination = 4
    if len(proposition_list) != taille_combination:
        print(f"Erreur : La combinaison doit avoir {taille_combination} couleurs.")
        return None
    
    # Valider que chaque couleur est valide
    color_accepted = ['vert', 'rouge', 'jaune', 'orange', 'blanc', 'violet']
    for color in proposition_list:
        if color not in color_accepted:
            print(f"Erreur : '{color}' n'est pas une couleur valide.")
            return None
    
    # Si tout est valide, retourner la proposition
    return proposition_list