from time import time
from math import *
from numpy import *
from random import *

##############
# SAE S01.01 #
##############

def nb_villes(villes):
    """Retourne le nombre de villes"""
    return len(villes)//3


def noms_villes(villes):
    """Retourne un tableau contenant le nom des villes"""
    noms_v = []
    i = 0
    while 3*i < len(villes):
        noms_v.append(villes[3*i])
        i += 1
    return noms_v


def d2r(nb):
    return nb*pi/180


def distance(long1, lat1, long2, lat2):
    """retourne la distance entre les points (long1, lat1) et (long2, lat2)"""
    lat1 = d2r(lat1)
    long1 = d2r(long1)
    lat2 = d2r(lat2)
    long2 = d2r(long2)
    R = 6370.7
    d = R*arccos(sin(lat1)*sin(lat2)+cos(lat1)*cos(lat2)*cos(long2-long1))
    return d


def indexCity(ville, villes):
    """Retourne l'indice dans le tableau villes de la ville de nom ville,
       et -1 si elle n'existe pas
    """
    res = -1
    i = 0
    while 3*i < len(villes) and villes[3*i] != ville:
        i += 1
    if 3*i < len(villes):
        res = 3*i
    return res


def distance_noms(nom1, nom2, villes):
    """Retourne la distance entre les villes nom1 et nom2 
       en fonction de la structure de données villes
    """
    index1 = indexCity(nom1, villes)
    index2 = indexCity(nom2, villes)

    if index1 == -1 or index2 == -1:
        d = -1
    else:
        d = distance(villes[index1+1], villes[index1+2],
                     villes[index2+1], villes[index2+2])
    return d


def lecture_villes(path):
    """Retourne la structure de données villes en fonction des données du fichier path"""
    f_in = open(path, encoding='utf-8', mode='r')
    villes = []
    li = f_in.readline()
    li = li.strip()
    while li != '':
        tab_li = li.split(';')
        villes.append(tab_li[0])
        villes.append(float(tab_li[1]))
        villes.append(float(tab_li[2]))
        li = f_in.readline()
        li = li.strip()
    f_in.close()
    return villes


def long_tour(villes, tournee):
    """Retourne la longueur d'une tournée en fonction de la structure de données villes"""
    long = 0
    i = 0
    while i+1 < len(tournee):
        long += distance_noms(tournee[i], tournee[i+1], villes)
        i += 1
    long += distance_noms(tournee[i], tournee[0], villes)
    return long

##############
# SAE S01.02 #
##############

# 1°/

tab = ["Paris",2.33, 48.86, "Lyon", 4.85, 45.75, "Marseille", 5.40, 43.30, "Lille", 3.06, 50.63]

def dictionary_cities(villes):
    """
    Paramètre(s): un tableau villes qui représente chaque ville par 3 éléments (nom, longitude et latitude)
    
    Cette fonction renvoie un dictionnaire contenant le nom des villes ainsi que leur distance par rapport aux autres villes
    """
    dico = {}
    for i in range(0, len(villes), 3): # Parcours les index de la liste villes
        dico[villes[i]] = {}
        for j in range(0, len(villes), 3): # Parcours les index de la liste villes
            if i != j: # On vérifie que les index i et j de la liste ville sont différents pour éviter les doublons 
                dico[villes[i]][villes[j]] = distance_noms(villes[i], villes[j], villes) # On utilise la fonction distance_noms afin de calculer la distance entre 2 villes 
    return dico # Renvoie le dictionnaire des distances


# 2°/

def distance_cities(name1, name2, d_cities):
    """
    Paramètre(s): deux chaînes de caractère name1 et name2 (noms de villes) et un dictionnaire représentant les distances entre chaque ville
    
    Cette fonction renvoie la distance entre les villes passées en paramètre si le nom des villes est présent dans le dictionnaire sinon elle renvoie -1
    """
    if name1 in d_cities: # Vérifie si la première ville est dans la liste
        if name2 in d_cities[name1]: # Vérifie si la deuxième ville est dans la liste
            return d_cities[name1][name2] # Retourne la distance entre les 2 villes
    return -1 # Si au moins une ville n'est pas dans la liste, elle retourne -1

# 3°/

def tour_length(tour, d_cities):
    """
    Paramètre(s): un tableau tour contenant le nom des villes (peu importe l'ordre) et un dictionnaire représentant les distances entre chaque ville
    
    Cette fonction renvoie la longueur étant représenté par la somme des distances entre les villes présentes dans le tableau tour en ajoutant le retour au point de départ
    """
    somme = 0
    for i in range(len(tour) - 1): # Parcours les index de la liste villes
        somme += distance_cities(tour[i], tour[i + 1], d_cities) # Ajoute la distance entre la ville d'index i et la ville d'index i+1 
    somme += distance_cities(tour[-1], tour[0], d_cities) # Ajoute la distance entre la dernière ville et la ville de départ
    return somme

# 5°/

def closest_city(city, cities, d_cities):
    """
    Paramètre(s): une chaîne de caractère city (nom d'une ville), un tableau cities contenant des noms de villes et un dictionnaire représentant les distances entre chaque ville
    
    Cette fonction renvoie l'index du tableau cities représentant la ville la plus proche de la ville représentée par la chaine de caractère city
    """
    index = 0
    distance = distance_cities(city, cities[0], d_cities) # Initialise la distance entre la ville city et la 1ère ville du tableau
    for i in range(1, len(cities)): # Parcours les index de la liste cities
        if distance_cities(city, cities[i], d_cities) < distance: # Vérifie si la nouvelle distance est inférieur à la distance actuelle
            distance = distance_cities(city, cities[i], d_cities)
            index = i # Stocke l'index i indiquant la ville la plus proche dans la variable index
    return index
    
# 6°/ 

def tour_from_closest_city(city, d_cities):
    """
    Paramètre(s): une chaîne de caractère city (nom d'une ville) et un dictionnaire représentant les distances entre chaque ville
    
    Cette fonction renvoie un tableau contenant le meilleur tour possible en fonction de la ville passé en paramètre (qui est donc le départ), et chaque ville est suivie de la ville restante la plus proche
    """
    villes = list(d_cities.keys()) # Créer une liste villes et stocke le nom des villes
    villes.remove(city) # On enlève le nom city pour éviter les erreurs
    tour = [city]
    
    for i in range(len(villes)): # Parcours les index de la liste villes
        index = closest_city(tour[i], villes, d_cities)
        tour.append(villes.pop(index)) # On rajoute dans tour ce qu'on enlève à l'index de la liste villes 
        
    return tour  

# 7°/

def best_tour_from_closest_city(d_cities):
    """
    Paramètre(s): un dictionnaire représentant les distances entre chaque ville
    
    Cette fonction renvoie un tableau contenant le meilleur tour possible en fonction de la somme des distances
    """
    best_tour = None
    best_distance = float('inf')  # Initialisé à l'infini

    for ville in d_cities.keys():  # Parcours le nom des villes parmi les clés du dictionnaire
        tour = tour_from_closest_city(ville, d_cities) # Créer le meilleur tour en fonction de la variable ville
        distance = tour_length(tour, d_cities) # Calcule la distance de ce tour

        if distance < best_distance: # Vérifie si la nouvelle distance est inférieur à la distance actuelle
            best_distance = distance
            best_tour = tour

    return best_tour # Renvoie le tableau avec le meilleur tour possible

# 9°/

def reverse_part_tour(tour, ind_b, ind_e):
    """
    Paramètre(s): un tableau tour contenant le nom des villes dans l'ordre alphabétique et deux indices, l'un de début et l'autre de fin (ind_b et ind_e)
    
    Cette fonction modifie le tableau tour passé en paramètre en inversant les éléments du sous tableau de tour situé entre les indices ind_b et ind_e inclus
    """
    while ind_b < ind_e: # Vérifie si la valeur d'ind_b est inférieur à celle d'ind_e
        tour[ind_b], tour[ind_e] = tour[ind_e], tour[ind_b] # Inverse l'index ainsi que la position des deux valeurs entre elles
        ind_b += 1
        ind_e -= 1


# 10°/

def inversion_length_diff(tour, d_cities, ind_b, ind_e):
    """
    Paramètre(s): un tableau tour contenant le nom des villes, un dictionnaire représentant les distances entre chaque ville et deux indices, l'un de début et l'autre de fin (ind_b et ind_e)
    
    Cette fonction renvoie la différence (float) entre la distance du tour passé en paramètre et celui obtenu en inversant les éléments du sous tableau de tour situé entre les indices ind_b et ind_e inclus
    """
    distance = tour_length(tour, d_cities)
    
    reversed_tour = tour.copy() # Fais une copie du tableau tour afin d'éviter toute modification 
    reverse_part_tour(reversed_tour, ind_b, ind_e)
    
    reversed_distance = tour_length(reversed_tour, d_cities)
    return distance - reversed_distance # Retourne la distance entre le tour passé en paramètre et celle inversé entre les indices

# 11°/

def better_inversion(tour, d_cities):
    """
    Paramètre(s): un tableau tour contenant le nom des villes, un dictionnaire représentant les distances entre chaque ville
    
    Cette fonction renvoie True si un tour avec une distance plus petite a été trouvée (et modifie tour), et renvoie False sinon
    """
    change = False # Initialisation par False
    for i in range(len(tour) - 1): # Parcours les index de la liste tour
        for j in range(i + 1, len(tour)): # Parcours les index de la liste tour en commençant par i+1

            diff = inversion_length_diff(tour, d_cities, i, j)

            if diff > 0: # Si diff est supérieur à 0 alors il existe une plus petite distance
                change = True # Stocke True dans la variable change vu que la condition est vraie
                reverse_part_tour(tour, i, j) # On effectue l'inversion à l'aide de la fonction reverse_part_tour 
                
    return change 

# 12°/

def best_obtained_with_inversions(tour, d_cities):
    """
    Paramètre(s): un tableau tour contenant le nom des villes, un dictionnaire représentant les distances entre chaque ville
    
    Cette fonction renvoie un entier qui est le nombre d'inversions effectuées afin de trouver le meilleur tour possible
    """
    nb_inversions = 0 # Initialise avec 0

    while better_inversion(tour, d_cities): # Vérifie que tant que cette condition est vraie, c'est-à-dire qu'on est au dessus de 0 
        nb_inversions += 1 # On incrémente de 1 à notre compteur 

    return nb_inversions 


