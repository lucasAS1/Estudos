Pn = float(input('Preço normal: '))
Ppromo = float(input('Preço promoção: '))
desc30 = Pn * 0.70
desc20 = Pn * 0.80

if(Ppromo < desc30):
    print('Dinheiro')
elif(Ppromo < desc20):
    print('Crédito à vista')
else:
    print('Crédito parcelado')
