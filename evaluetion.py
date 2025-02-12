
# confronto di tipo 



# except

int()
float()
str()
bool()

b = input('input :')
try:    
    b = int(b)
except:
    b = str(b)

c = input('input :')
try:    
    c = int(c)
except:
    c = str(c)

type(b) == int and type(c) == int

print(type(b))
print(type(b) == int and type(c) == int)

