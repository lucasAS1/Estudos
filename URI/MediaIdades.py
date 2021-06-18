x = int(input())
ages = 0
i = 0

while x > 0:
    ages+=x
    x = int(input())
    i += 1

print(f'{ages/i:.2f}')