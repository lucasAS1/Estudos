def exibir(v,n):
    i = 0
    while i < n-1:
        print(v[i],end=' ')
        i += 1
    
    print(v[i])

    return

def empurra(v, n):
    i = 0

    while i < n-1:
        if v[i] > v[i+1]:
            troca(v,i,i+1)
        i += 1
    
    return

def troca(v, i, j):
    temp = v[i]
    v[i] = v[j]
    v[j] = temp

    return

def bubble_sort(v, n):
    tam = n
   
    while tam > 1:
        empurra(v,tam)
        tam -= 1

    return

v = input().split()

if len(v) > 1:
    for n in range(0,len(v)):
        v[n] = int(v[n])
    bubble_sort(v,len(v))

linha = ''

while linha != 'encerrar':
    linha = input().split()

    if linha[0] == 'exibir':
        exibir(v,len(v))
    elif linha[0] == 'adicionar':
        v.append(int(linha[1]))
        bubble_sort(v,len(v))
    elif linha[0] == 'remover':
        try:
            v.pop(v.index(int(linha[1])))
        except:
            print(f'código {linha[1]} não encontrado')
    elif linha[0] == 'encerrar':
        exibir(v,len(v))
        break