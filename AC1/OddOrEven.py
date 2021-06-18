# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
a = int(input())

if((a+1)%2!=0):
    resMax = a + 2
    resMin = a - 1
else:
    resMax = a + 1
    resMin = a - 2


print(f"{resMin} {resMax}")