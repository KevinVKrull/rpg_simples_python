import random

def escolha_acao():
    print('--------------- OPÇOES ---------------')
    print('')
    print('            Escolha sua ação:')
    print('1 -🌀 Rajada Temporal: (5 de mana, 10-15 Dano)')
    print('2 -⏳ Fenda do Tempo: (15 de mana 20-30 Dano)')
    print('3 -🔁 Ressurgir Temporal: (40 de mana, volta 2 turnos no tempo reverte histórico de status)')
    print('4 -🛡️  Defender: (50% redução de dano do próximo ataque do boss)')
    print('5 -❤️  Poção de Vida: (restaura de 20-30 de vida)')
    print('6 -🔮 Poção de Mana: (restaura de 25-35 de mana)')
    print('')

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