num = int(input('Numero: '))
result = 1
for f in range(1, num + 1):
    result *= f
print('{}! = {}'.format(num, result))
   