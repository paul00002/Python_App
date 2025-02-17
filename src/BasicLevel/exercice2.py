# 2. **Generatore di istogrammi**  
#    Data una lista di numeri, genera istogrammi con asterischi corrispondenti al valore. Salva il risultato in un file txt
# Lista di numeri
numeri = [5, 3, 9, 7, 2, 6]

# Apre il file "istogramma.txt" in modalità scrittura
with open("istogramma.txt", "w") as file:
    # Per ogni numero nella lista, crea una riga dell'istogramma
    for numero in numeri:
        # Genera la stringa di asterischi
        istogramma = "*" * numero
        file.write(istogramma + "\n")

print("L'istogramma è stato salvato in 'istogramma.txt'")
