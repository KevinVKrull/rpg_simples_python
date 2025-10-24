import random

def magias_boss(vida_jogador,defesa,chance_lorde,chance_atual_lorde):
    if chance_lorde < chance_atual_lorde:
        tipo = 'explosao'
        print('Lorde Sombrio: usou ☄️  EXPLOSÃAAAAO DO CAAAAOS ☄️')
        if defesa:
            dano_lorde = int((vida_jogador / 2) / 2)
            print(f'🛡️  Defesa do Mago do Tempo ativada!, voce perdeu apenas {dano_lorde} de Vida.')
        else:
            dano_lorde = int(vida_jogador / 2)
            print(f'Voce perdeu {dano_lorde} de Vida')

        vida_jogador -= dano_lorde
        explosao = True
        chance_atual_lorde = 30

    else:
        tipo = 'soco'
        dano_lorde = random.randint(10, 20)
        print(f'Lorde Sombriu: usou seu 👊 Soco Sombrio. 👊')
        print(f'Dano Lorde Sombrio: {dano_lorde}')
        if defesa:
            dano_lorde = int(dano_lorde / 2)
            print(f'🛡️  Defesa do Mago Ativada, voce recebeu {dano_lorde} de dano')
        else:
            print(f'Lorde Sombrio causou {dano_lorde} de dano.')

        vida_jogador -= dano_lorde
        explosao = False
        chance_atual_lorde += 20

    defesa = False
    return vida_jogador, explosao, defesa, dano_lorde, chance_atual_lorde, tipo