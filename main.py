import time
import random
import acoes
import boss
import boss_voltar_magias
import magias_jogador
import copy
import gerador_mapas
import boss_andar


mago_do_tempo = {
    "nome": "Mago do Tempo",
    "vida": 150,
    "mana": 120,
    'vida_maxima': 150,
    'mana_maxima': 120,
    "defesa": False,
    'armadura': 0,
    'moedas_iniciais': 50,
    'velocidade': 5,
    'inventario': [],

}

lorde_sombrio = {
    "nome": "Lorde Sombrio",
    "vida":1,
    "chance_explosao": 30,
    'explosao':False,
}

historico = []
ataques_boss = []
ataques_boss_repetir = []
andar = 1
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
    print(historico)
    mostrar_status(mago_do_tempo, lorde_sombrio, turno)
    acoes.escolha_acao()
    print(ataques_boss)
    print(ataques_boss_repetir)

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
    
    # ---------- REPETIR MAGIAS BOSS---------- 
    if len(ataques_boss_repetir) > 0:
        ataques_boss_repetir, mago_do_tempo = boss_voltar_magias.boss_voltar_magias(ataques_boss_repetir,mago_do_tempo)
    else:  
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
    

    continuar = input('Aperte ENTER para continuar: ')
    turno += 1
    historico_turno = {
            "turno": turno,
            "mago_do_tempo": mago_do_tempo.copy(),
            "lorde_sombrio": lorde_sombrio.copy()
        }
    historico.append(historico_turno)
    acoes.apagar()
    '''
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
    '''
    

#---- SAIU DO PRIMEIRO WHILE
#-----------------------------------------------------------------------------
acoes.texto()
acoes.continuar_para_torre1(andar)
#-----------------------------------------------------------------------------
mapa, mapa_nome = gerador_mapas.gerar_mapa()
pos_l, pos_c = 0, 0

mapa_visivel = gerador_mapas.mapa_visivel()
mapa_visivel[pos_l][pos_c] = mapa_nome[pos_l][pos_c]
salas_resolvidas = gerador_mapas.salas_resolvidas()

while True:
    if andar != 1:
        break

    acoes.apagar()
    print(mago_do_tempo['inventario'])
    print(f'Voce esta na Sala {mapa_nome[pos_l][pos_c]}')
    print('')

    for linha in mapa_visivel:
        print(linha)

    print('1')
    if mapa_nome[pos_l][pos_c] == 'Escadas':
        print("🎉 Você encontrou as escadas 🎉")
        print('No momento em que voce sobe um BOSS aparece em sua frente...\n' \
        'Sua missao atual: Derrote o Guardião de Pedra!')

        boss_derrotado = gerador_mapas.enfrentar_boss()
        break

    # ----- ENTRA NA CONDIÇÃO DE SE ENTROU NA SALA -----
    if not salas_resolvidas[pos_l][pos_c]:

        salas_resolvidas[pos_l][pos_c] = True
        sala_atual = mapa_nome[pos_l][pos_c]
        print(sala_atual)

        if sala_atual == 'Combate':
            print('Voce entrou em um combate, Enfrente o Guardião de Pedra!')
            gerador_mapas.enfrentar_guardiao(boss_andar.magoo_do_tempo,boss_andar.guardiao_de_pedra)

        elif sala_atual == 'Tesouro':
            print('Voce entrou em uma sala de Tesouro')
            mago_do_tempo = gerador_mapas.tesouro(mago_do_tempo)

        elif sala_atual == 'Mercador':
            print('Voce encontrou um Mercador')
            gerador_mapas.mercador()
        elif sala_atual == 'Descanso':
            print('Voce achou um lugar para Recuperar suas Energias')
            gerador_mapas.sala_descanso()
        elif sala_atual == 'Evento':
            print('Sala de Evento')
            gerador_mapas.evento()

    else:
        print('Voce ja passou por essa sala')
    # ---------------------------------------------------------------------------
    
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


    pos_l, pos_c = nova_l, nova_c
    mapa_visivel[pos_l][pos_c] = mapa[pos_l][pos_c]