x = int(input())
array = []

for i in range(0,x+1):
    if i % 2 != 0:
        array.append(i)
for i in array:
    print(i)