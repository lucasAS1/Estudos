x = int(input())
y = 0
y = x * (x-1)

for i in range(2,x):
    y = y * (x - i)

print(y)