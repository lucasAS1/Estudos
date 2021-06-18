x = int(input())
y = int(input())
i = 0

while x > 0:
    i += 1
    print(f'pagamento: {i}')
    print(f'antes = {x}')
    x = x - y
    if x < 0:
        print(f'depois = 0')
    else:
        print(f'depois = {x}')
    
    print(f'-----')
