import time
import random
import acoes
import boss
import boss_voltar_magias
import magias_jogador

vida_jogador = 150
mana_jogador = 120
vida_boss = 10
historico = []
chance_atual_lorde = 30
explosao = False
defesa = False
ataques_boss = []
ataques_boss_repetir = []
andar = 0

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
        acoes.apagar()
        continue
    
    # ---------- MAGIAS ----------
    if escolha == '1':
        mana_jogador, vida_boss, sucesso = magias_jogador.rajada_temporal(mana_jogador, vida_boss)
        if not sucesso:
            time.sleep(2)
            acoes.apagar()
            continue

    if escolha == '2':
        mana_jogador, vida_boss, sucesso = magias_jogador.fenda_do_tempo(mana_jogador, vida_boss)
        if not sucesso:
            time.sleep(2)
            acoes.apagar()
            continue

    # ---------- VOLTAR NO TEMPO ----------
    if escolha == '3':
        mana_jogador, vida_jogador, vida_boss, ataques_boss_repetir, ataques_boss, historico = magias_jogador.ressurgir_temporal(mana_jogador, vida_jogador, vida_boss, ataques_boss_repetir, ataques_boss, historico)
        turno -= 2
        time.sleep(2)
        acoes.apagar()
        continue
        

    # ---------- DEFESA ----------
    if escolha == '4':
        print('Mago do Tempo: Ativou sua Defesa 🛡️')
        defesa = True

    # ---------- POÇÃO ----------
    if escolha == '5':
        vida_jogador = magias_jogador.usar_pocao_vida(vida_jogador)
    elif escolha == '6':
        mana_jogador = magias_jogador.usar_pocao_mana(mana_jogador)

    time.sleep(1)

    print('')
    time.sleep(1.5)

    chance_lorde = random.randint(1, 100)
    print(f'Chance roletada: {chance_lorde}')
    print('')
    
    # ---------- REPETIR MAGIAS BOSS---------- 
    if len(ataques_boss_repetir) > 0:
        ataques_boss_repetir, vida_jogador, defesa = boss_voltar_magias.boss_voltar_magias(ataques_boss_repetir,vida_jogador,defesa)
        
    else:
        # ---------- EXPLOSAO BOSS----------
        if chance_lorde < chance_atual_lorde:
            vida_jogador, explosao, defesa, dano_lorde, chance_atual_lorde, tipo = boss.magias_boss(vida_jogador,defesa,chance_lorde,chance_atual_lorde)

        # ---------- SOCO SIMPLES BOSS----------        
        else:
            vida_jogador, explosao, defesa,dano_lorde,chance_atual_lorde,tipo = boss.magias_boss(vida_jogador, defesa,chance_lorde, chance_atual_lorde)
        
        ataques_boss.append({'turno': turno,'tipo':tipo ,'dano_lorde':dano_lorde})

    # ---------- VITORIA OU DERROTA----------
    if vida_jogador <= 0:
        print('')
        print('Mago do Tempo morreu, Loooorde das Sombras Venceu!')
        time.sleep(3)
        break
    elif vida_boss <= 0:
        print('')
        print('Lorde das Sombras morreu, Mago do Tempo saiu vivo!')
        andar = 1
        time.sleep(3)
        break


    continuar = input('[S/N]: ')

    if continuar in 'Ss':
        turno += 1
        historico_turno = {'turno':turno,'vida_jogador': vida_jogador , 'mana_jogador':mana_jogador , 'vida_boss':vida_boss, 'chance_atual_lorde':chance_atual_lorde} 
        historico.append(historico_turno)
        acoes.apagar()
        continue
    else:
        acoes.apagar()
        print('Voce fugiu, COVARDE!')
        break
#-----------------------------------------------------------------------------
acoes.texto()
acoes.continuar_para_torre1(andar)
#-----------------------------------------------------------------------------
mapa = acoes.gerar_mapa()
pos_l, pos_c = 0, 0
    
mapa_visivel = acoes.mapa_visivel()
mapa_visivel[pos_l][pos_c] = mapa[pos_l][pos_c]

while True:
    if andar == 1:
        break
    
    print(f'Voce esta na Sala {mapa[pos_l][pos_c]}')
    print('')
    for linha in mapa_visivel:
        print(linha)

    if mapa[pos_l][pos_c] == 'Escadas':
        print("🎉 Você encontrou as escadas e completou o andar!")
        break

    comando = input("Mover (W/A/S/D) ou 'sair': ").strip().lower()
    
    nova_l, nova_c = pos_l, pos_c
    if comando == 'w' and pos_l > 0:
        nova_l -= 1
    elif comando == 's' and pos_l < 2:
        nova_l += 1
    elif comando == 'a' and pos_c > 0:
        nova_c -= 1
    elif comando == 'd' and pos_c < 2:
        nova_c += 1
    elif comando == 'sair':
        print("Saindo do jogo...")
        break
    else:
        print("Movimento inválido!")
        continue
    
    # Atualizar posição e revelar a sala no mapa visível
    pos_l, pos_c = nova_l, nova_c
    mapa_visivel[pos_l][pos_c] = mapa[pos_l][pos_c]
