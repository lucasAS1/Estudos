x = 100
y = 200
i = 0
vezesBD = 0
vezesBT = 0

while i < x :
    print('bom dia')
    vezesBD +=1
    j = 0
    while j < y:
        print('boa tarde')
        vezesBT +=1
        j += 1
    else:
        i += 1

print('boa noite')
print(f'bom dia:{vezesBD},boa tarde:{vezesBT}')