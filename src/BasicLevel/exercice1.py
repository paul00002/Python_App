# 1. **Max tra due numeri**  
#    Chiedi due numeri all'utente e stampa il maggiore usando istruzioni `if/else`.

#x=int(input("inserirsci il primo numero:"))
#print(x,type(x))
#y=int(input("inserisci il secondo numero:"))
#print(y,type(y))
#so che tipo di variabili sono sia x e y in più le ho visualizzate a video. 

#funzione + controllo degli errori 
def chiedi_numero():
    while True:
        try:
            numero = int(input("Inserisci un numero intero: "))
            return numero
        except ValueError:
            print("Errore: devi inserire un numero intero!")

# Chiedi i due numeri all'utente
numero1 = chiedi_numero()
numero2 = chiedi_numero()

# Confronta i numeri e stampa il maggiore
if numero1 > numero2:
    print(f"Il numero maggiore è: {numero1}")
elif numero2 > numero1:
    print(f"Il numero maggiore è: {numero2}")
else:
    print("I due numeri sono uguali.")

#finito