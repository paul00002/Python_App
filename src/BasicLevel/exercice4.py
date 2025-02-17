# 4. **Scambio variabili**  
#    Leggi un file json e modificalo con l'input del utente
''' cose da fare in poche parole 

1. Leggere il contenuto di un file JSON.
2. Modificare il contenuto del JSON in base all'input dell'utente.
3. Salvare di nuovo il file JSON con i dati modificati.

'''
#with open ("Data/file.json","r") as file: #il file non si trova nella stessa cartella, scrivo DATA/ per trovarlo.
#    print(file.read()) #visualizzazione a video di cosa contiene il file json.
file=open("Data/file.json","r")
print(c=file.read())
#print(c)
file2=open("Data/file.json","r")
file2.read()
print(file.read(),file2.read())