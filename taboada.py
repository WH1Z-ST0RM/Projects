print('Taboada')
num = int(input('Multiplos de: '))
print('**********')
for tab in range(0, 2):
  var = tab * num
  print(f'{num} x {tab} = 0{var}')
for tab in range(2, 10):
  var = tab * num
  print(f'{num} x {tab} = {var}')
print('**********')
