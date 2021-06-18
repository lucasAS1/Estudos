def bubble_sort(v, n):
    tam = n
   
    while tam > 1:
        empurra(v,tam)
        tam -= 1

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

def exibe(v, n):
    i = 0

    while i < n:
        print(v[i],end=' ')
        i += 1

    print('\n')

    return
l = [40,20,50,30,10]
bubble_sort(l,5)
exibe(l,5)
