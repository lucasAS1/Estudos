x = int(input())
y = int(input())
soma = []
calc = 0

for i in range(y+1,x):
    if i % 2 != 0:
        soma.append(i)
for i in soma:
    calc=calc + i

print(calc)