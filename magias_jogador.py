import random
import time
import acoes

def rajada_temporal(mago_do_tempo, lorde_sombrio):
    if mago_do_tempo['mana'] >= 5:
        dano_mago = random.randint(10, 15)
        mago_do_tempo['mana'] -= 5
        lorde_sombrio['vida'] -= dano_mago
        print(f'Mago do Tempo: usou sua RAJADAAA TEMPORALES causando ⚔️  {dano_mago} de Dano no Lorde Sombrio.')
        return mago_do_tempo, lorde_sombrio, True
    elif mago_do_tempo['mana'] < 5:
        print(f'Essa magia custa 💧 5 de mana! Mana atual {mago_do_tempo['mana']}, Tenta Novamente! ')
        return mago_do_tempo, lorde_sombrio, False

def fenda_do_tempo(mago_do_tempo, lorde_sombrio):
    if mago_do_tempo['mana'] >= 15:
        dano_mago = random.randint(20, 30)
        mago_do_tempo['mana'] -= 15
        lorde_sombrio['vida'] -= dano_mago
        print(f'Mago do Tempo: usou sua Fenda do Tempo causando ⚔️  {dano_mago} de Dano no Lorde Sombrio.')
        return mago_do_tempo, lorde_sombrio, True
    elif mago_do_tempo['mana'] < 15:   
        print(f'Essa magia custa 💧 15 de mana! Mana atual {mago_do_tempo['mana']}, Tenta Novamente! ')
        return mago_do_tempo, lorde_sombrio, False
    

def usar_pocao_vida(mago_do_tempo):
    cura = random.randint(20, 30)
    nova_vida = min(mago_do_tempo["vida"] + cura, mago_do_tempo['vida_maxima'])
    print(f'Mago do Tempo: recuperou ❤️  {nova_vida - mago_do_tempo["vida"]} de vida!')
    mago_do_tempo["vida"] = nova_vida
    return mago_do_tempo

def usar_pocao_mana(mago_do_tempo):
    mana = random.randint(25, 35)
    nova_mana = min(mago_do_tempo['mana'] + mana, 100)
    print(f'Mago do Tempo: recuperou 💧  {nova_mana - mago_do_tempo['mana']} de mana!')
    mago_do_tempo['mana'] = nova_mana
    return mago_do_tempo

def ressurgir_temporal(mago_do_tempo, lorde_sombrio, ataques_boss_repetir, ataques_boss, historico):
    if mago_do_tempo['mana'] < 40:
        print(f'Essa magia custa 40 de mana, voce tem apenas {mago_do_tempo['mana']} no momento.') 
        return mago_do_tempo, lorde_sombrio, ataques_boss_repetir, ataques_boss, historico, False
    
    if len(historico) < 3:
        print('Voce precisa de pelo menos 2 turnos a mais para usar essa magia!')  
        return mago_do_tempo, lorde_sombrio, ataques_boss_repetir, ataques_boss, historico, False
    
    if mago_do_tempo['mana'] >= 40:
        mago_do_tempo['mana'] -= 40

        mago_do_tempo = historico[-3]['mago_do_tempo']
        lorde_sombrio = historico[-3]['lorde_sombrio']
        print('🔁  Mago do Tempo usou ressurgir')

        ataques_boss_repetir = ataques_boss[-2:]
        ataques_boss = ataques_boss[:-2]
        historico = historico[:-2]
        time.sleep(2)
        acoes.apagar()
        return mago_do_tempo, lorde_sombrio, ataques_boss_repetir, ataques_boss, historico, True