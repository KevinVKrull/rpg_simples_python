import gerador_mapas
import bau_de_tesouro
import mercador_itens
import acoes
import jogador.jogador_atual as jogador_atual
import boss_atual
import combate_andar
import time
import eventos


def combate_primeiro_andar():
    mapa, mapa_nome = gerador_mapas.gerar_mapa()
    pos_l, pos_c = 0, 0

    mapa_visivel = gerador_mapas.mapa_visivel()
    mapa_visivel[pos_l][pos_c] = mapa_nome[pos_l][pos_c]
    salas_resolvidas = gerador_mapas.salas_resolvidas()
    estoque_andar1 = None

    while True:
        if jogador_atual.mago_do_tempo['andar_atual'] != 1:
            break

        acoes.apagar()
        print(jogador_atual.mago_do_tempo['inventario'])
        print(jogador_atual.mago_do_tempo)
        print(f'Voce esta na Sala {mapa_nome[pos_l][pos_c]}')
        print('')

        for linha in mapa_visivel:
            print(linha)

        print('1')
        if mapa_nome[pos_l][pos_c] == 'Escadas':
            print("🎉 Você encontrou as escadas 🎉")
            print('No momento em que voce sobe um BOSS aparece em sua frente...\n' \
            'Sua missao atual: Derrote o Guardião de Pedra!')

            break

        # ----- ENTRA NA CONDIÇÃO DE SE ENTROU NA SALA -----
        if not salas_resolvidas[pos_l][pos_c]:

            salas_resolvidas[pos_l][pos_c] = True
            sala_atual = mapa_nome[pos_l][pos_c]
            print(sala_atual)

            if sala_atual == 'Combate':
                vitoria = None
                print('Voce entrou em um combate, Enfrente o Guardião de Pedra!')
                time.sleep(2)
                acoes.apagar()
                vitoria, vida_atual = combate_andar.enfrentar_guardiao(jogador_atual.mago_do_tempo, boss_atual.guardiao_de_pedra, None)
                if vitoria:
                    print('VOCEEE VENCEEEU')
                    jogador_atual.mago_do_tempo = vida_atual
                else:
                    print('F PARA VOCE')
                    break

            elif sala_atual == 'Tesouro':
                print('Voce entrou em uma sala de Tesouro')
                jogador_atual.mago_do_tempo = bau_de_tesouro.tesouro(jogador_atual.mago_do_tempo)

            elif sala_atual == 'Mercador':
                print('Voce encontrou um Mercador')
                jogador_atual.mago_do_tempo, estoque_andar1  = mercador_itens.mercador(jogador_atual.mago_do_tempo, estoque_andar1)

            elif sala_atual == 'Descanso':
                print('Voce achou um lugar para Recuperar suas Energias')
                gerador_mapas.sala_descanso()

            elif sala_atual == 'Evento':
                print('Sala de Evento')
                jogador = eventos.sala_de_evento(jogador_atual.mago_do_tempo)

        else:
            # ---------- OPÇÃO PRA CASO O JOGADOR QUEIRA VOLTAR NESSAS 2 SALAS ----------
            if sala_atual == 'Mercador':
                print('Voce encontrou um Mercador')
                jogador_atual.mago_do_tempo, estoque_andar1 = mercador_itens.mercador(jogador_atual.mago_do_tempo, estoque_andar1)

            elif sala_atual == 'Descanso':
                print('Voce achou um lugar para Recuperar suas Energias')
                gerador_mapas.sala_descanso()

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