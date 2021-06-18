a = 0
b = []
soma = 0
media = 0
a = int(input())

while a >= 0:
    soma += a
    b.append(a)
    a = int(input())

media = soma / len(b)
print(f'MEDIA: {media:.2f}')

for i in range(0,len(b)):
    if b[i] < media:
        print(b[i])