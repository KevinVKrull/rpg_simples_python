import random
import time
import acoes

def rajada_temporal(mana_atual, vida_boss):
    if mana_atual >= 5:
        dano_mago = random.randint(10, 15)
        mana_atual -= 5
        vida_boss = vida_boss - dano_mago
        print(f'Mago do Tempo: usou sua RAJADAAA TEMPORALES causando ⚔️  {dano_mago} de Dano no Lorde Sombrio.')
        return mana_atual, vida_boss, True
    elif mana_atual < 5:
        print(f'Essa magia custa 💧 5 de mana! Mana atual {mana_atual}, Tenta Novamente! ')
        return mana_atual, vida_boss, False

def fenda_do_tempo(mana_atual, vida_boss):
    if mana_atual >= 15:
        dano_mago = random.randint(20, 30)
        mana_atual -= 15
        print(f'Mago do Tempo: usou sua Fenda do Tempo causando ⚔️  {dano_mago} de Dano no Lorde Sombrio.')
        vida_boss = vida_boss - dano_mago
        return mana_atual, vida_boss, True
    elif mana_atual < 15:   
        print(f'Essa magia custa 💧 15 de mana! Mana atual {mana_atual}, Tenta Novamente! ')
        return mana_atual, vida_boss, False
    

def usar_pocao_vida(vida_atual):
    cura = random.randint(20, 30)
    nova_vida = min(vida_atual + cura, 120)
    print(f'Mago do Tempo: recuperou ❤️  {nova_vida - vida_atual} de vida!')
    return nova_vida

def usar_pocao_mana(mana_atual):
    mana = random.randint(25, 35)
    nova_mana = min(mana_atual + mana, 100)
    print(f'Mago do Tempo: recuperou 💧  {nova_mana - mana_atual} de mana!')
    return nova_mana

def ressurgir_temporal(mana_jogador, vida_jogador, vida_boss, ataques_boss_repetir, ataques_boss, historico):
    if mana_jogador < 40:
        print(f'Essa magia custa 40 de mana, voce tem apenas {mana_jogador} no momento.')
        time.sleep(2)
        acoes.apagar()
    if len(historico) < 3:
        print('Voce precisa de pelo menos 2 turnos a mais para usar essa magia!')
        time.sleep(2)
        acoes.apagar()
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
    return mana_jogador, vida_jogador, vida_boss, ataques_boss_repetir, ataques_boss, historico