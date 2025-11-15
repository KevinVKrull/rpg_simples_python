import random

def magias_boss(mago_do_tempo,lorde_sombrio, chance_lorde):
    if chance_lorde < lorde_sombrio['chance_explosao']:
        tipo = 'explosao'
        print('Lorde Sombrio: usou ☄️  EXPLOSÃAAAAO DO CAAAAOS ☄️')
        if mago_do_tempo['defesa']:
            dano_lorde = int((mago_do_tempo['vida'] / 2) / 2)
            print(f'🛡️  Defesa do Mago do Tempo ativada!, voce perdeu apenas {dano_lorde} de Vida.')
        else:
            dano_lorde = int(mago_do_tempo['vida'] / 2)
            print(f'Voce perdeu {dano_lorde} de Vida')

        mago_do_tempo['vida'] -= dano_lorde
        lorde_sombrio['explosao'] = True
        lorde_sombrio['chance_explosao'] = 30

    else:
        tipo = 'soco'
        dano_lorde = random.randint(10, 20)
        print(f'Lorde Sombriu: usou seu 👊 Soco Sombrio. 👊')
        print(f'Dano Lorde Sombrio: {dano_lorde}')
        if mago_do_tempo['defesa']:
            dano_lorde = int(dano_lorde / 2)
            print(f'🛡️  Defesa do Mago Ativada, voce recebeu {dano_lorde} de dano')
        else:
            print(f'Lorde Sombrio causou {dano_lorde} de dano.')

        mago_do_tempo['vida'] -= dano_lorde
        lorde_sombrio['explosao'] = False
        lorde_sombrio['chance_explosao'] += 20

    mago_do_tempo['defesa'] = False
    return mago_do_tempo, lorde_sombrio, dano_lorde, tipo