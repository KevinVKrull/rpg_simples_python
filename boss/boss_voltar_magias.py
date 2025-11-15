def boss_voltar_magias(ataques_boss_repitir, mago_do_tempo):
    ataque = ataques_boss_repitir.pop(0)
    print(ataque)
    print(ataques_boss_repitir)
    if ataque['tipo'] == 'soco':
        if mago_do_tempo['defesa']:
            mago_do_tempo['vida'] -= int(ataque['dano_lorde'] / 2)
            print('Lorde Sombriu: usou 👊  Soco Sombrio 👊')
            print(f'🛡️  Defesa Ativada!, voce recebeu {ataque['dano_lorde'] / 2} de dano')
            mago_do_tempo['defesa'] = False
        else:
            mago_do_tempo['vida'] -= ataque['dano_lorde']
            print(f'Lorde Sombriu: usou 👊  Soco Sombrio 👊 causando {ataque['dano_lorde']} de dano')
    elif ataque['tipo'] == 'explosao':
        if mago_do_tempo['defesa']:
            print('Lorde Sombrio: usou ☄️  EXPLOSÃAAAAO DO CAAAAOS ☄️')
            ataque['dano_lorde'] = int((mago_do_tempo['vida'] / 2) / 2)
            print(f'🛡️  Defesa Ativada!, voce recebeu {ataque['dano_lorde']} de dano')
            mago_do_tempo['vida'] -= ataque['dano_lorde']
            mago_do_tempo['defesa'] = False
        else:
            print('Lorde Sombrio: usou ☄️  EXPLOSÃAAAAO DO CAAAAOS ☄️')
            print(f'Voce recebeu {ataque['dano_lorde']} de dano')
            mago_do_tempo['vida'] -= ataque['dano_lorde']
    return ataques_boss_repitir, mago_do_tempo