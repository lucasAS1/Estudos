def invertido(n):
    if n == 0: print(n)
    while n!=0:
        print(n % 10, end='')
        n = n // 10
