a = float(input())
b = int(input())

descountPercentage = 0.90 - (b / 100)

print(f"{(a * b):.2f}")
print(f"{(descountPercentage * (a * b)):.2f}")
