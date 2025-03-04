# 3. **Somma numeri naturali**  
#    Continua a leggere numeri e sommarli finché non viene inserito 0.
somma = 0

while True:
    numero = int(input("Inserisci un numero (0 per fermarti): "))
    
    if numero == 0:
        break
    
    somma = somma + numero

print("Somma totale:", somma)
#finito