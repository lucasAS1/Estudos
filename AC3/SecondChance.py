tent = int(input())
notas = []
notasComplementares = []
notasAlteradas = []
cont = 1
contAlteradas = 0

for i in range(0,tent):
    notas.append(float(input()))

for x in range(0,tent):
    notasComplementares.append(float(input()))
    if notasComplementares[x] == 10 and notas[x] <= 8:
        notasAlteradas.append(notas[x] + 2)
        contAlteradas+=1
    elif notasComplementares[x] == 10 and notas[x] != 10:
        notasAlteradas.append(10)
        contAlteradas+=1
    else:
        notasAlteradas.append(0)

print(f'NOTAS ALTERADAS: {contAlteradas}')

for p in range(0,tent):
    if notasAlteradas[p] > notas[p]:
        print(f'*({cont:0>3}) original: {notas[p]:05.2f} | final: {notasAlteradas[p]:05.2f}')
    else:
        print(f'-({cont:0>3}) original: {notas[p]:05.2f} | final: {notas[p]:05.2f}')
    cont+=1