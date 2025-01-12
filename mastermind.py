import random
#Fonction qui génère une combinaison sécrètede couleur

def generate_combination(taille=4):
    # Liste des couleurs acceptées
    color_accepted = ['vert', 'rouge', 'jaune', 'orange', 'blanc', 'violet']

    # Génère une combinaison aléatoire de la taille spécifiée
    alea = [random.choice(color_accepted) for _ in range(taille)]
    
    return alea
