a = int(input())
b = int(input())
i = 0
if b >= a:
    for x in range(a,b+1):
        while i < 10:
            i+=1
            print(f"{x} x {i} = {x*i}")
        i = 0
        print('----------')
else:
    print('Nenhuma tabuada no intervalo!')