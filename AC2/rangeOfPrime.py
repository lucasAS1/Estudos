x = int(input())
y = int(input())
cont = 0

for i in range(x,y+1):
    if i>1:
        for z in range(2,i):
            if(i % z) == 0:
                break
        else:
            cont+=1
            print(i) 
print(f'primos: {cont}')

