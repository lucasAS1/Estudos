n1 = 10
n2 = 5

if n1%11==1:
    print('primeiro if verdadeiro')
    if n1%2==1:
        n2=n1+10.5
    else:
        n1=n2+10
else:
    n1=n1%11
    print('primeiro if falso')
    
    if n1%2==0 and n1%2==1:
        print('segundo if verdadeiro')
        n2=n1+5
print(n2)
n2=n2//2+5*n2//3
print(n1)
print(n2)
print(n1+n2%2)
