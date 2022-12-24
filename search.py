#!/bin/python3
from googlesearch import search
q = input("Ingrese su busqueda: ")
results = search(q, 30)
for r in results:
        print(r)
