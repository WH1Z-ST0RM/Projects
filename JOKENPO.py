import random

Type = ['Pedra', 'Papel', 'Tesoura']
bot = random.choice(Type)

player = input('Jogue: [Pedra, Papel, Tesoura] ')
if player == 'Pedra' :
  print('Você jogou Pedra!')
  
  if bot == 'Papel' :
    print('O computador jogou Papel')
    print('Você perdeu!')
    
  elif bot == 'Tesoura' :
    print('')
    print('Você ganhou!')
  else :
    print('O computador jogou Pedra')
    print('Empate!')

if player == 'Papel' :
  print('Você jogou Papel!')
  
  if bot == 'Tesoura' :
    print('O computador jogou Tesoura')
    print('Você perdeu!')
    
  elif bot == 'Pedra' :
    print('O computador jogou Pedra')
    print('Você ganhou!')
    
  else :
    print('O computador jogou Papel')
    print('Empate!')
    
if player == 'Tesoura' :
  print('Você jogou Tesoura!')
  
  if bot == 'Pedra' :
    print('O computador jogou Pedra')
    print('Você perdeu!')
    
  elif bot == 'Papel' :
    print('O computador jogou Papel')
    print('Você ganhou!')
    
  else :
    print('O computador jogou Tesoura')
    print('Empate!')