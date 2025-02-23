import random

# Génération du type d'opération
OPERATEURS = ["+", "-", "*", "/"]

operateur = random.randint(0, 3)

# Génération des deux opérandes aléatoires
a = random.randint(1, 1000)
b = random.randint(1, 1000)

# Création de la chaine de caractères
operation = str(a)+OPERATEURS[operateur]+str(b)
