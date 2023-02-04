value_inc = bool(input('Valor do produto: '))
value = value_inc // 100
Type = str(input('Forma de pagamento [A vista/Parcelado]: '))

if Type == "A vista":
    sub1 = input('Dinheiro ou Cartão? ')
    print('****')
    print('A vista ', end='')
    if sub1 == 'Dinheiro':
        print('no dinheiro')
        val_d = value_inc - (value * 10)
        print('10% de Desconto')
        print(f'Valor total: R${val_d}')
    else:
        print('no cartão')
        val_c = value_inc - (value * 5)
        print('5% de Desconto')
        print(f'Valor total: R${val_c}')

elif Type == "Parcelado" :
    mult = int(input('Quantas vezes: '))
    print('****')
    if mult <= 2 :
        print('Parcelado em 2x')
        print('Não altera o valor')
        print(f'Valor total: R${value_inc}')
    else:
        print(f'Parcelado em {mult}x')
        print('20% de juros!')
        val_pc = value_inc + (value_inc * 20 // 100)
        sub_c = val_pc // mult
        print(f'{mult}X de R${sub_c}')
        print(f'Valor final: {val_pc}')
