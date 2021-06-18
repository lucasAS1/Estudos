i = int(input())
a = []

for x in range(0,i):
    a.append(input().split(';'))

taxaPremium = float(input())
taxaPobre = float(input())

print('-----\nBÔNUS\n-----')

for canal in a:
    bonoros = 0
    contBonus = 0
    inscritos = int(canal[1])

    while inscritos >= 1000:
        inscritos -= 1000
        contBonus += 1

    if canal[3] == 'sim':
            bonoros = (contBonus * taxaPremium) + float(canal[2])
    else:
            bonoros = (contBonus * taxaPobre) + float(canal[2])

    print(f'{canal[0]}: R$ {bonoros:.2f}')