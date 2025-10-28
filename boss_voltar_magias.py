def boss_voltar_magias(ataques_boss_repitir, vida_jogador, defesa):
    ataque = ataques_boss_repitir.pop(0)
    print(ataque)
    print(ataques_boss_repitir)
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
    return ataques_boss_repitir, vida_jogador, defesa