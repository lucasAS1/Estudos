a = input()
b = int(input())

semana = ['domingo', 'segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado']
diaDaSemana = semana[semana.index(a)]

if(b == 0):
    print(f"chega hoje!")
elif((b + semana.index(a)) >= 6):
    b = (b + semana.index(a)) - 7
    print(f"sera entregue {semana[b]}")
else:
    print(f"sera entregue {semana[semana.index(diaDaSemana) + b]}")