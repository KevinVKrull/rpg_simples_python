import time
import random
import acoes
import boss
import boss_voltar_magias
import magias_jogador



mago_do_tempo = {
    "nome": "Mago do Tempo",
    "vida":100,
    "mana":100,
    'vida_maxima':200,
    "defesa":False,
}

lorde_sombrio = {
    "nome": "Lorde Sombrio",
    "vida": 10,
    "chance_explosao": 30,
    'explosao':False,
}

historico = []
ataques_boss = []
ataques_boss_repetir = []
andar = 0
turno = 1
print('')



def mostrar_status(mago_do_tempo, lorde_sombrio, turno):
    print(f'\n--------------- TURNO {turno} ---------------\n')
    print(f'🧙 {mago_do_tempo['nome']} = ❤️  {mago_do_tempo['vida']}')
    print(f'🧙 {mago_do_tempo['nome']} = 💧 {mago_do_tempo['mana']}')
    print(f'🧙 {mago_do_tempo['nome']} = 🛡️  {mago_do_tempo['defesa']}')
    print(f'💀 {lorde_sombrio['nome']} = 🤍 {lorde_sombrio['vida']}')
    print(f'🎲 Chance atual do Lorde Sombrio: {lorde_sombrio['chance_explosao']}')

historico_turno = {
        "turno": turno,
        "mago_do_tempo": mago_do_tempo.copy(),
        "lorde_sombrio": lorde_sombrio.copy()
    }
historico.append(historico_turno)

while True:
    mostrar_status(mago_do_tempo, lorde_sombrio, turno)
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
        mago_do_tempo, lorde_sombrio, sucesso = magias_jogador.rajada_temporal(mago_do_tempo, lorde_sombrio)
        if not sucesso:
            time.sleep(2)
            acoes.apagar()
            continue

    if escolha == '2':
        mago_do_tempo, lorde_sombrio, sucesso = magias_jogador.fenda_do_tempo(mago_do_tempo, lorde_sombrio)
        if not sucesso:
            time.sleep(2)
            acoes.apagar()
            continue

    
    # ---------- VOLTAR NO TEMPO ----------
    if escolha == '3':
        mago_do_tempo, lorde_sombrio, ataques_boss_repetir, ataques_boss, historico, sucesso = magias_jogador.ressurgir_temporal(mago_do_tempo, lorde_sombrio, ataques_boss_repetir, ataques_boss, historico)
        if sucesso:
            turno = max(1, turno - 2)
            
        time.sleep(2)
        acoes.apagar()
        continue
        

    # ---------- DEFESA ----------
    if escolha == '4':
        print('Mago do Tempo: Ativou sua Defesa 🛡️')
        mago_do_tempo['defesa'] = True

    # ---------- POÇÃO ----------
    if escolha == '5':
        mago_do_tempo = magias_jogador.usar_pocao_vida(mago_do_tempo)
    elif escolha == '6':
        mago_do_tempo = magias_jogador.usar_pocao_mana(mago_do_tempo)
    
    time.sleep(1)

    print('')
    time.sleep(1.5)

    chance_lorde = random.randint(1, 100)
    print(f'Chance roletada: {chance_lorde}')
    print('')
    '''
    # ---------- REPETIR MAGIAS BOSS---------- 
    if len(ataques_boss_repetir) > 0:
        ataques_boss_repetir, mago_do_tempo = boss_voltar_magias.boss_voltar_magias(ataques_boss_repetir,mago_do_tempo)
    '''   
        # ---------- EXPLOSAO BOSS----------
    mago_do_tempo, lorde_sombrio, dano_lorde, tipo = boss.magias_boss(mago_do_tempo, lorde_sombrio, chance_lorde)
    ataques_boss.append({'turno': turno,'tipo':tipo ,'dano_lorde':dano_lorde})
    
    # ---------- VITORIA OU DERROTA----------
    if mago_do_tempo['vida'] <= 0:
        print('')
        print('Mago do Tempo morreu, Loooorde das Sombras Venceu!')
        time.sleep(3)
        break
    elif lorde_sombrio['vida'] <= 0:
        print('')
        print('Lorde das Sombras morreu, Mago do Tempo saiu vivo!')
        andar = 1
        time.sleep(3)
        break
    

    continuar = input('[S/N]: ')

    if continuar in 'Ss':
        turno += 1
        historico_turno = {
            "turno": turno,
            "mago_do_tempo": mago_do_tempo.copy(),
            "lorde_sombrio": lorde_sombrio.copy()
        }
        historico.append(historico_turno)
        acoes.apagar()
        continue
    else:
        acoes.apagar()
        print('Voce fugiu, COVARDE!')
        break

#---- SAIU DO PRIMEIRO WHILE
#-----------------------------------------------------------------------------
acoes.texto()
acoes.continuar_para_torre1(andar)
#-----------------------------------------------------------------------------
mapa = acoes.gerar_mapa()
pos_l, pos_c = 0, 0
    
mapa_visivel = acoes.mapa_visivel()
mapa_visivel[pos_l][pos_c] = mapa[pos_l][pos_c]

while True:
    if andar != 1:
        break
    
    print(f'Voce esta na Sala {mapa[pos_l][pos_c]}')
    print('')
    for linha in mapa_visivel:
        print(linha)

    if mapa[pos_l][pos_c] == 'Escadas':
        print("🎉 Você encontrou as escadas 🎉")
        print('No momento em que voce sobe um BOSS aparece em sua frente...\n' \
        'Sua missao atual: Derrote o Guardião de Pedra!')

        boss_derrotado = acoes.enfrentar_boss()
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
    acoes.apagar()


    
