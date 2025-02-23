#!/usr/bin/env python3

import sys
from os import isatty

arguments = sys.argv[1:] 
operators = ("+","-","/","*")

def parseAndCalculus(input:str):
    # ERROR HANDELIND HERE
    findedOperator = None;
    for i in range(len(operators)):
        operatorIndex = input.find(operators[i])
        if operatorIndex != -1: 
            findedOperator = operators[i]
            break
    
    if not findedOperator: 
        printStdout("Merci d'entrer un opération mathématique de la forme: x[+,-,*,/]y")
        sys.exit(1)

    try:
        firstOperand = int(input[:operatorIndex].strip())
        secondOperand = int(input[operatorIndex+1:].strip())
    except: 
        printStdout("Les deux opérateur douvent être des nombres")
        sys.exit(1)

    match findedOperator:
        case "+": return addition(firstOperand,secondOperand)
        case "-": return soustraction(firstOperand,secondOperand)
        case "/": return division(firstOperand,secondOperand)
        case "*": return multiplication(firstOperand,secondOperand)


def addition(op1, op2):
    return op1+op2;
def multiplication(op1, op2):
    return op1*op2;
def soustraction(op1, op2):
    return op1-op2;
def division(op1, op2):
    # Handle /0 error
    return op1/op2;

def printStdout(textToPrint:str):
    sys.stdout.write(textToPrint)
    sys.stdout.flush()

def interactiveMinitrice():
    
    printStdout("> ")
    try:
        for line in sys.stdin:
            if len(line) !=0:         
                printStdout(str(parseAndCalculus(line))+"\n")
                
            printStdout("> ")
    except KeyboardInterrupt :
        printStdout("\nFin des calculs !")
        sys.exit(0)



if not isatty(sys.stdin.fileno()):
    printStdout(str(parseAndCalculus(str(sys.stdin.read()))))
    sys.exit(0)
else: 
    interactiveMinitrice()
   



