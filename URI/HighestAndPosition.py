num = []

for i in range(0,10):
    num.append(int(input()))

print(max(num))
print(num.index(max(num))+1)