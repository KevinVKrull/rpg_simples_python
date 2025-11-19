import jogador.jogador_atual as jogador_atual
from collections import deque
import random
import time
import acoes
import copy

def enfrentar_boss():
    print('')

# ---------- ENFRENTAR GUARDIAO ---------------------
def enfrentar_guardiao(mago_do_tempo, guardiao_de_pedra, vitoria):
    mago_do_tempo_atual = copy.deepcopy(mago_do_tempo)
    guardiao_de_pedra_atual = copy.deepcopy(guardiao_de_pedra)

    fila_movimentos = deque()

    if mago_do_tempo_atual['velocidade'] > guardiao_de_pedra_atual['velocidade']:
        fila_movimentos.append(mago_do_tempo_atual)
        fila_movimentos.append(guardiao_de_pedra_atual)
    else:
        fila_movimentos.append(guardiao_de_pedra_atual)
        fila_movimentos.append(mago_do_tempo_atual)

    while True:
        print('-> Mago do Tempo:')
        print(f'  Vida = ❤️  {mago_do_tempo_atual['vida']}')
        print(f'  Mana = 💧  {mago_do_tempo_atual['mana']}')
        print(f'  Defesa = 🛡️  {mago_do_tempo_atual['defesa']}')
        print('-------------------------------------------------------------')
        print('-> Guardiao de Pedra: ')
        print(f'  Vida = 🤍  {guardiao_de_pedra_atual['vida_atual']}')

        turno = fila_movimentos[0]

        acoes_disponiveis = ['atacar', 'defender', 'pocao']

    # ----------------- MAGIA DO JOGADOR ------------------
        if turno == mago_do_tempo_atual:
            i = 0
            while i < 2:
                print(i)
                print('Escolha sua ação: ')
                print('')
                
                for index, acao in enumerate(acoes_disponiveis, 1):
                    print(f'{index} - {acao}')

                escolha = input(' ->  ')

                try:
                    escolha = acoes_disponiveis[int(escolha) - 1]
                except:
                    print('Opçãp invalida.')
                    continue

                if escolha == 'atacar':
                    acoes.ataque()
                    opcao_magia = input('Escolha qual magia voce quer usar: ')

                #------------ MAGIAS ------------
                    if int(opcao_magia) > 2 or int(opcao_magia) < 1:
                        print('Opcao Invalida, Tente Novamente!')
                        continue   
                    elif opcao_magia == '1':
                        dano = random.randint(10, 15)
                        print(f'Mago do Tempo deu {dano} de dano')
                        guardiao_de_pedra_atual['vida_atual'] -= dano
                        i += 1
                        time.sleep(1)
                    elif opcao_magia == '2':
                        dano = random.randint(20, 30)
                        print(f'Mago do Tempo deu {dano} de dano')
                        guardiao_de_pedra_atual['vida_atual'] -= dano
                        i += 1
                        time.sleep(1)

                #------------ DEFESA ------------
                elif escolha == 'defender':
                    mago_do_tempo_atual['defesa'] = True
                    print('🛡️ Defesa Ativada!')
                    i += 1

                #------------ POÇÃO ------------
                elif escolha == 'pocao':
                    acoes.pocao()
                    opcao_magia = input('QUal poção voce gostaria de usar?: ')
                #------------ CURA ------------
                    if opcao_magia == '1':
                        cura = random.randint(20, 30)
                        mago_do_tempo_atual['vida'] = min(mago_do_tempo_atual['vida'] + cura, mago_do_tempo_atual['vida_maxima'])
                        print(mago_do_tempo_atual['vida'])
                        i += 1
                #------------ MANA ------------
                    elif opcao_magia == '2':
                        print('Magia de Mana')
                        i += 1
    
                acoes_disponiveis.remove(escolha)

    # ------------------ MAGIA DO BOSS ----------------------
        else:
            if mago_do_tempo_atual['defesa'] == True:
                dano = random.randint(15, 25)
                dano = dano / 2
                print(f'Guardiao de Pedra deu {dano} de dano')
                mago_do_tempo_atual['vida'] -= dano
                mago_do_tempo_atual['defesa'] = False
                time.sleep(2)
            else:
                dano = random.randint(15, 25)
                print(f'Guardiao de Pedra deu {dano} de dano')
                mago_do_tempo_atual['vida'] -= dano

        
        fila_movimentos.popleft()
        fila_movimentos.append(turno)

        if mago_do_tempo_atual['vida'] <= 0:
            print('Mago do Tempo morreu...')
            time.sleep(1)
            return False, mago_do_tempo_atual
        elif guardiao_de_pedra_atual['vida_atual'] <= 0:
            print('Guardiao de Pedra Morreu...')
            time.sleep(1)
            return True, mago_do_tempo_atual

        time.sleep(1)
        acoes.apagar()
        