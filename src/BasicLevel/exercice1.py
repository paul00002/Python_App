# 1. **Max tra due numeri**  
#    Chiedi due numeri all'utente e stampa il maggiore usando istruzioni `if/else`.

#n=input("Max tra due numeri")
#print(n)
x=int(input("inserirsci il primo numero:"))
print(x,type(x))
#print(x)
y=int(input("inserisci il secondo numero:"))
print(y,type(y))
#so che tipo di variabili sono sia x e y in più le ho visualizzate a video. 

if x and y ==int: 
    if x>y:
        print("il primo valore è maggiore del secondo"+str(x))
    elif x<y :
        print("il secondo valore è maggiore del primo"+str(y))
    elif x==y:
        print(" i due  numeri sono uguali")
        
