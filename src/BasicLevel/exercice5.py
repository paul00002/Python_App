### Livello Avanzato
#1. **Matrici inverse
#  Verifica che il prodotto tra una matrice e la sua inversa dia la matrice identità.
import random

def matrix(x, y):
    matrix = []
    
    for i in range(x):
        n = []
        for j in range(y):
            number = random.randint(1, 100)
            n.append(number)  
        matrix.append(n)  

    return matrix

print(matrix(3, 3))















