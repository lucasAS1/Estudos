x = int(input())
y = int(input())
i = 0
while x <= y:
    if x % 4 == 0 and (x % 100 != 0 or x % 400 == 0):
        i+=1
        print(x)
    x+=1
print(f'bissextos: {i}')