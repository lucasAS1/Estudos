a, b = input().split()

if(a > b):
    res = int(b) % int(a)
else:
    res = int(a) % int(b)
    
if(a == b):
    print('Sao Multiplos')
elif(res != 0):
    print('Nao sao Multiplos')
else:
    print('Sao Multiplos')