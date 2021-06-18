x = int(input())
alfabeto = chr(65)

for _ in range(1,x+1):
    temp ='';
    for i in range(0, _):
        temp+=alfabeto
    print(temp)
    alfabeto=chr(65+_)
    
