def devolveMaior100(T):

    t = []

    for num in T:
        if int(num)>99:
            t.append(int(num))

    return t

T = input().split()

print(devolveMaior100(T))

