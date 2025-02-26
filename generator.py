from os import isatty
import sys
import random

OPERATEURS = ["+", "-", "*", "/"]

# Vérification du pipe
is_pipe = not isatty(sys.stdin.fileno())
if is_pipe:
    nb_operations = int(sys.stdin.read())
elif len(sys.argv) > 1:
    nb_operations = int(sys.argv[1])
else:
    nb_operations = int(input("Combien d'operations souhaitez-vous genener : "))

# Génération des opérations
for i in range(nb_operations):
    a = random.randint(1,1000)
    b = random.randint(1,1000)

    op = OPERATEURS[random.randint(0,3)]
    print(str(a)+op+str(b))
