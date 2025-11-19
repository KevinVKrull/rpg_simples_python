import random
import time

def sala_de_evento(mago_do_tempo):
    opcoes = ['fonte', 'armadilha',]
    evento = random.choice(opcoes)

    while True:
        if evento == 'fonte':
            print('Voce encontou uma Fonte Mistaca!')
            print('Escolha um desses bonus!')
            bonus = ['+ 30 de vida', '+ 40 de mana', '+ 60 de moeda']

            for index, b in enumerate(bonus, 1):
                print(f'{index} -> {b}')

            e = input('Escolha: ')

            if e == '1':
                print('Voce se curou sua vida')
                cura = min(mago_do_tempo['vida'] + 30, mago_do_tempo['vida_maxima'])
                print(f'Voce curou {cura - mago_do_tempo['vida_maxima']} de vida')
                mago_do_tempo['vida'] = cura
                break
            elif e == '2':
                mana = min(mago_do_tempo['mana'] + 40, mago_do_tempo['mana_maxima'])
                print(f'Voce curou {mana - mago_do_tempo['mana_maxima']} de mana')
                mago_do_tempo['mana'] = mana
                break
            elif e == '3':
                print('Voce ganhou 60 moedas')
                mago_do_tempo['moedas_iniciais'] += 60
                break
        elif evento == 'armadilha':
            sua_sorte = random.randint(0, 100)
            print('Rolando o Dado do AZAR...')
            time.sleep(3)
            print(f'Numero Roletado: {sua_sorte}')
            if sua_sorte > 50:
                print('SORTE GRANDE!')
                print('Voce Evitou a Armadilha')
                break
            else:
                print('Zero Sorte...')
                dano = random.randint(25, 40)
                print(f'Voce tomou {dano} de dano')
                mago_do_tempo['vida'] = dano
      
      