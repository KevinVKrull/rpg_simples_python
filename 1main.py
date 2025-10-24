import os
import time
import random
import acoes
import boss

vida_jogador = 120
mana_jogador = 100
vida_boss = 200
historico = []
chance_atual_lorde = 50
explosao = False
defesa = False
ataques_boss = []
ataques_boss_repetir = []



def apagar():
    if os.name == 'nt':  
        os.system('cls')
    else: 
        os.system('clear')
     
        

turno = 1
print('')

historico_turno = {'turno':turno,'vida_jogador': vida_jogador , 'mana_jogador':mana_jogador , 'vida_boss':vida_boss, 'chance_atual_lorde':chance_atual_lorde} 
historico.append(historico_turno)

while True:
    print(f'--------------- TURNO {turno} ---------------')
    print('')

    print(f'🧙❤️  Vida Jogador = {vida_jogador}')
    print(f'🧙💧 Mana Jogador = {mana_jogador}')
    print(f'💀🤍 Vida Boss = {vida_boss}')
    print(f'🎲 Chance atual do Lorde Sombrio: {chance_atual_lorde} ')
    print('')

    acoes.escolha_acao()

    escolha = input('-> Escolha sua ação entre (1 a 6): ')
    print('')

    if escolha  not in ['1','2','3','4','5','6']:
        print('Opção errada tente novamente!')
        time.sleep(2)
        apagar()
        continue
    
    # ---------- MAGIAS ----------
    if escolha == '1':
        mana_jogador, vida_boss, sucesso = acoes.rajada_temporal(mana_jogador, vida_boss)
        if not sucesso:
            time.sleep(2)
            apagar()
            continue

    if escolha == '2':
        mana_jogador, vida_boss, sucesso = acoes.fenda_do_tempo(mana_jogador, vida_boss)
        if not sucesso:
            time.sleep(2)
            apagar()
            continue

    # ---------- VOLTAR NO TEMPO ----------
    if escolha == '3':
        if mana_jogador < 40:
            print(f'Essa magia custa 40 de mana, voce tem apenas {mana_jogador} no momento.')
            time.sleep(2)
            apagar()
            continue
        if len(historico) < 3:
            print('Voce precisa de pelo menos 2 turnos a mais para usar essa magia!')
            time.sleep(2)
            apagar()
            continue

        if mana_jogador >= 40:
            mana_jogador -= 40
            reversao_tempo = historico[-3]

            vida_jogador = reversao_tempo['vida_jogador']
            mana_jogador = reversao_tempo['mana_jogador']
            vida_boss = reversao_tempo['vida_boss']
            print('🔁  Mago do Tempo usou ressurgir')

            ataques_boss_repetir = ataques_boss[-2:]
            ataques_boss = ataques_boss[:-2]
            historico = historico[:-2]

            turno -= 2
            time.sleep(2)
            apagar()
            continue


    # ---------- DEFESA ----------
    if escolha == '4':
        print('Mago do Tempo: Ativou sua Defesa 🛡️')
        defesa = True

    # ---------- POÇÃO ----------
    if escolha == '5':
        vida_jogador = acoes.usar_pocao_vida(vida_jogador)
    elif escolha == '6':
        mana_jogador = acoes.usar_pocao_mana(mana_jogador)

    time.sleep(1)

    print('')
    time.sleep(1.5)

    chance_lorde = random.randint(1, 100)
    print(f'Chance roletada: {chance_lorde}')
    print('')
    

    if len(ataques_boss_repetir) > 0:
        ataque = ataques_boss_repetir.pop(0)
        print(ataque)
        print(ataques_boss_repetir)
        if ataque['tipo'] == 'soco':
            if defesa:
                vida_jogador -= int(ataque['dano_lorde'] / 2)
                print('Lorde Sombriu: usou 👊  Soco Sombrio 👊')
                print(f'🛡️  Defesa Ativada!, voce recebeu {ataque['dano_lorde'] / 2} de dano')
                defesa = False
            else:
                vida_jogador -= ataque['dano_lorde']
                print(f'Lorde Sombriu: usou 👊  Soco Sombrio 👊 causando {ataque['dano_lorde']} de dano')

        elif ataque['tipo'] == 'explosao':
            if defesa:
                print('Lorde Sombrio: usou ☄️  EXPLOSÃAAAAO DO CAAAAOS ☄️')
                ataque['dano_lorde'] = int((vida_jogador / 2) / 2)
                print(f'🛡️  Defesa Ativada!, voce recebeu {ataque['dano_lorde']} de dano')
                vida_jogador -= ataque['dano_lorde']
                defesa = False
            else:
                print('Lorde Sombrio: usou ☄️  EXPLOSÃAAAAO DO CAAAAOS ☄️')
                print(f'Voce recebeu {ataque['dano_lorde']} de dano')
                vida_jogador -= ataque['dano_lorde']
    else:
        # ---------- EXPLOSAO ----------
        if chance_lorde < chance_atual_lorde:
            vida_jogador, explosao, defesa, dano_lorde, chance_atual_lorde, tipo = boss.magias_boss(vida_jogador,defesa,chance_lorde,chance_atual_lorde)

        # ---------- SOCO SIMPLES ----------        
        else:
            vida_jogador, explosao, defesa,dano_lorde,chance_atual_lorde,tipo = boss.magias_boss(vida_jogador, defesa,chance_lorde, chance_atual_lorde)
        
        ataques_boss.append({'turno': turno,'tipo':tipo ,'dano_lorde':dano_lorde})

    if vida_jogador <= 0:
        print('')
        print('Mago do Tempo morreu, Loooorde das Sombras Venceu!')
        time.sleep(2.5)
        break
    elif vida_boss <= 0:
        print('')
        print('Lorde das Sombras morreu, Mago do tempo retorna a sua Vila Vivo!')
        time.sleep(2.5)
        break


    continuar = input('[S/N]: ')

    if continuar in 'Ss':
        turno += 1
        historico_turno = {'turno':turno,'vida_jogador': vida_jogador , 'mana_jogador':mana_jogador , 'vida_boss':vida_boss, 'chance_atual_lorde':chance_atual_lorde} 
        historico.append(historico_turno)
        apagar()
        continue
    else:
        apagar()
        print('Voce fugiu, COVARDE!')
        break

  
