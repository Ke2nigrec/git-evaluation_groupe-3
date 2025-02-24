import random
from sys import stdin
from os import isatty

# Vérifier si il y a un paramètre dans le pipe, sinon demander a la saisie
is_pipe = not isatty(stdin.fileno())

if is_pipe :
    nb_op = stdin.read()
else:
    nb_op = input("Combien d'operations ? ")




for i in range(nb_op):
    # Génération du type d'opération
    OPERATEURS = ["+", "-", "*", "/"]

    operateur = random.randint(0, 3)

    # Génération des deux opérandes aléatoires
    a = random.randint(1, 1000)
    b = random.randint(1, 1000)

    # Création de la chaine de caractères et envoi sur la sortie par défaut
    print(str(a)+OPERATEURS[operateur]+str(b))
