#!/usr/bin/env python
"""Imprime a tabuada do 1 ao 10."""
__version__="0.1.0"
__author__="Hugo Carvalho"

#numeros = [1,2,3,4,5,6,7,8,9,10]
numeros = list(range(1,11))
#print(numeros)
#Iterable (percorriveis)
for numero in numeros:
    print("{:-^18}".format(f"Tabuada do {numero}:"))
    print()
    for outro_numero in numeros:
        resultado = numero * outro_numero
        print("{:^18}".format(f"{numero} x {outro_numero} = {resultado}"))
        print()
    print("#" * 18)
    print()
