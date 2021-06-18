x = 0;
total = 0;
x = float(input())
vicCoin = 0

while x != -1.0:
    vicCoin += x
    total = vicCoin * 2.5   
    x = float(input())

print(f'VC$ {vicCoin:.2f}')
print(f'R$ {total:.2f}')