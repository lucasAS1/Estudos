n1, n2, n3, n4 = input().split();

n1 = float(n1) * 2
n2 = float(n2) * 3
n3 = float(n3) * 4
n4 = float(n4)

media = ((n1+n2+n3+n4)/10)
print(f'Media: {media:.1f}')

if(media >= 7):
    print('Aluno aprovado.')
elif(media >= 5):
    print('Aluno em exame.')
    
    exame = float(input())
    print(f'Nota do exame: {exame:.1f}')
    media = (media + exame) / 2
    if(media >= 5):
        print(f'Aluno aprovado.')
        print(f'Media final: {media:.1f}')
else:
    print('Aluno reprovado.')