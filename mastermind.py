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

#comparaison des combinaisons 
def combination_comparison(combination, proposition): 
    color_well_placed = 0
    color_badly_placed = 0  #Compteur pour les couleurs bien et mal placées

    secret_copy = combination.copy()
    proposition_copy = proposition.copy()

    #vérifier les couleurs à la bonne position 
    for i in range(len(combination)):
        if proposition_copy[i] == secret_copy[i]:
            color_well_placed += 1 
            secret_copy[i] = None #couleur trouvée

    #vérifier les couleurs à la mauvaise position
    for i in range(len(proposition)):
        if proposition_copy[i] != secret_copy[i] and proposition_copy[i] in secret_copy:
            color_badly_placed += 1 
            secret_copy[secret_copy.index(proposition_copy[i])] =None 
           
#retourne les couleurs
    return color_well_placed, color_badly_placed  