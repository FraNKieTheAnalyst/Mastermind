import random
from collections import Counter 
import tkinter as tk  # Interface graphique simple
import pygame  # Pour des graphismes interactifs 

# fonction qui génère une combinaison secrète de couleur
def combination(taille=4): 
    color_accepted = ['vert', 'rouge', 'jaune', 'vert', 'orange', 'blanc', 'violet']
    alea = [random.choice(color_accepted) for index in range(taille)]
    print(alea)
    
#Demande au joueur sa proposition de combinaison de couleur

def player_proposition():
        proposition = input("Enter your proposition")
        print("your proposition is :", proposition)

#Convertir la saisie du joueur en liste de couleur
proposition_list = proposition.lower().split() 

# verification de la saisie du joueur
if len(proposition_list)==4 and all(color in color_accepted for color in proposition_list):
      print("Your proposition is correct:", proposition_list)
      return proposition_list
else  print("proposition invalid")
       print (accepted_color)

#comparaison des combinaisons
couleurs_bien_placées = 0 # Compteur pour les couleurs bien placées
couleurs_mal_places = 0

secret_copy = alea.copy() 
proposition_copy = proposition.copy()

# Vérifier les couleurs à la bonne position (correspondance exacte)
 for i in range(len(alea)): 
          if proposition[i] == alea[i]:
             couleurs_bien_placées += 1  
             secret_copy[i] = None # Marquer cette couleur comme trouvée

# Vérifier les couleurs correctes mais mal placées
for i in range(len(proposition)):
         if proposition[i] != alea[i] and proposition[i] in secret_copy:
                couleurs_mal_places += 1
                secret_copy[secret_copy.index(proposition[i])] = None # Retirer la couleur pour éviter les doublons

return couleurs_bien_placées, couleurs_mal_places



        
