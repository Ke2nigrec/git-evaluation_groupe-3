#!/usr/bin/env python3

import sys
from os import isatty

# Liste des opérateurs 
operators = ("+","-","/","*")

# Parse le string et calcul 
def parseAndCalculus(input:str):
    # ERROR HANDELIND needed HERE
    
    # Trouve l'opérateur dans le string en paramètre 
    findedOperator = None;
    for i in range(len(operators)):
        operatorIndex = input.find(operators[i])
        if operatorIndex != -1: 
            findedOperator = operators[i]
            break
    
    # Vérification synthaxique, retourne une erreur si il n'y a pas d'opérateur detecté
    if not findedOperator: 
        printStdout("Merci d'entrer un opération mathématique de la forme: x[+,-,*,/]y")
        sys.exit(1)

    # Permet de vérifier si les paramètres sont des entiers (à changer en fonction du code, pour prendre des float aussi par exemple)
    try:
        firstOperand = int(input[:operatorIndex].strip())
        secondOperand = int(input[operatorIndex+1:].strip())
    
    except: 
        printStdout("Les deux opérateur douvent être des nombres entiers")
        sys.exit(1)

    # Appel la bonne fonction selon l'opérateur detecté
    match findedOperator:
        case "+": return addition(firstOperand,secondOperand)
        case "-": return soustraction(firstOperand,secondOperand)
        case "/": return division(firstOperand,secondOperand)
        case "*": return multiplication(firstOperand,secondOperand)


# Gère les opération de base (+,-,/,*)
def addition(op1, op2):
    return op1+op2;
def multiplication(op1, op2):
    return op1*op2;
def soustraction(op1, op2):
    return op1-op2;
def division(op1, op2):
    # Handle /0 error
    return op1/op2;

# Permet d'afficher le string en paramètre sur la sortie stdout
def printStdout(textToPrint:str):
    sys.stdout.write(textToPrint)
    sys.stdout.flush()

# Gère les entrées sur le CLI pour calculer les expressions
def interactiveMinitrice():
    printStdout("> ")
    try:
        for line in sys.stdin:
            if len(line) !=0:         
                printStdout(str(parseAndCalculus(line))+"\n")
                
            printStdout("> ")
    except KeyboardInterrupt :
        # Si l'utilisateur fait ctrl + D (ctrl + C)
        printStdout("\nFin des calculs !")
        sys.exit(0)


# Vérifie la présence ou non de pipeline
if not isatty(sys.stdin.fileno()):
    # Affiche le résultat de l'opération en entrée du programme
    printStdout(str(parseAndCalculus(str(sys.stdin.read()))))
    # Retourne que le programme s'est bien déroulé
    sys.exit(0)
else: 
    # Si il n'y a pas de pipeline on lance le mode interatif
    interactiveMinitrice()
   



