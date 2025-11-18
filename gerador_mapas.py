import random
import boss_atual
import bau_de_tesouro
import combate_andar
import mercador_itens

#--------------------- GERADOR DE MAPA COM EMOTE --------------------
def gerar_mapa():
    possiveis_salas = ['Combate','Descanso','Tesouro','Mercador','Evento']
    pesos = [0, 0, 0, 0, 100]

    emojis = {
        'Inicio': '🏠',
        'Combate': '⚔️ ',
        'Tesouro': '💰',
        'Mercador': '🧑',
        'Descanso': '🛌',
        'Evento': '🎲',
        'Escadas': '🪜',
        }

    mapa = []
    mapa_nome = []

    for l in range(3):
        lista = []
        lista_nomes = []

        for c in range(3):
            if l == 0 and c == 0:
                sala = 'Inicio'
            elif l == 2 and c == 2:
                sala = 'Escadas'
            else:
                sala = random.choices(possiveis_salas, weights=pesos)[0] # faz a parte de chance de cair algo e depois transforma em uma string

            lista.append(emojis[sala])
            lista_nomes.append(sala)

        mapa.append(lista)
        mapa_nome.append(lista_nomes)

    return mapa, mapa_nome

#--------------------- MAPA VISIVEL --------------------
def mapa_visivel():
    mapa_visivel = []
    for l in range(3):
        linha = []
        for c in range(3):
            linha.append('?')  # sala ainda não visitada
        mapa_visivel.append(linha)
    return mapa_visivel


def salas_resolvidas():
    salas_resolvidas = []
    for _ in range(3):
        lista = []
        for _ in range(3):
            lista.append(False)
        salas_resolvidas.append(lista)
    return salas_resolvidas

# ---------- ENFRENTAR BOSS ---------------------
def enfrentar_boss():
    print('')

# ---------- SALA DESCANSO ---------------------
def sala_descanso():
    print('')
