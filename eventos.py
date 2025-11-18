import random

def sala_de_evento():
    #'armadilha', 'altar'
    opcoes = ['fonte', 'fonte', 'fonte']
    evento = random.choice(opcoes)

    while True:
        if evento == 'fonte':
            print('Voce encontou uma Fonte Mistaca!')
            print('Escolha um desses bonus!')
            bonus = ['+ 30 de vida', '+ 40 de mana', '+ 60 de moeda']
            for index, b in enumerate(bonus, 1):
                print(f'{index} -> {b}')
            e = input('Escolha: ')

            try:
                e = bonus[int(e) - 1]
            except:
                print('Escolha invalida!')
                continue

            print(e)
      
      