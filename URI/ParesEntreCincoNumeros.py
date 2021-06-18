lista = []
lista.append(int(input()))
lista.append(int(input()))
lista.append(int(input()))
lista.append(int(input()))
lista.append(int(input()))

pares = 0

for seila in lista:
    if(seila % 2 == 0):
        pares += 1

print(f'{pares} valores pares')
    
