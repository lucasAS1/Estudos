numero = int(input())
soma = 0
cont = 0
i = 0

while(cont < numero):
    if i % 2 == 0:
        soma+=i
        cont+=1
    i += 1

print(soma)