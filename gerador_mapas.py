import random
import boss_atual
import bau_de_tesouro
import combate_andar
import mercador_itens

#--------------------- GERADOR DE MAPA COM EMOTE --------------------
def gerar_mapa():
    possiveis_salas = ['Combate','Descanso','Tesouro','Mercador','Evento']
    pesos = [0, 0, 0, 100, 0]

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

# ---------- ENFRENTAR GUARDIAO ---------------------
def enfrentar_guardiao(mago_do_tempo, guardiao_de_pedra):
    while True:
        print('1')

'''    
# ---------- TESOUROS ---------------------
def tesouro(mago_do_tempo):
    item = bau_de_tesouro.bau_de_madeira()
    chance = random.randint(0,100)
    chance_mimic = 10
    print(item)
    print(chance)
    
    
    abrir = input('Voce encontrou um bau, deseja abri-lo? [S/N]: ').lower()
    if abrir == 's' and chance <= chance_mimic:
        print('Um mimic surgiu')
        return mago_do_tempo
    elif abrir == 's' and chance > chance_mimic:
        print(f'Voce encontrou um(a):')
        print('')
        for i, c in item.items():
            print(f'{i}: {c}')
        print('')

        continuar = input('Guardar Item no Inventario? [S/N]: ').lower()

        if continuar == 's':
            if len(mago_do_tempo['inventario']) < 10:
                mago_do_tempo['inventario'].append(item)
                print('voce guardou o item no inventario')
            else:
                print('Voce esta com o inventario cheio')
        else:
            print('Voce jogou no chao')
    return mago_do_tempo

'''
'''
# ---------- MERCADOR DE ITENS ---------------------
def mercador(mago_do_tempo, estoque_existente=None):

    if estoque_existente is not None:
        estoque = estoque_existente
    else:
        estoque = mercador_ambulante()

    while True:
        print('')
        for i, item in enumerate(estoque, start=1):
            print(f'{i} Item: {item['nome']}, preco: {item['preco']}, tipo: {item['tipo']}')

        escolha = input("Digite o número do item para comprar ou 'sair': ").lower()

        if escolha == "sair":
            print("Você saiu da loja. Até a próxima!")
            break

        if not escolha.isdigit():
            print("❌ Escolha inválida! Digite um número.")
            continue

        indice = int(escolha) - 1
        if indice < 0 or indice >= len(estoque):
            print("❌ Item não existe!")
            continue
        
        item = estoque[indice]
        mago_do_tempo['inventario'].append(item)
        estoque.pop(indice)
        break
    return mago_do_tempo, estoque
'''
# ---------- SALA DESCANSO ---------------------
def sala_descanso():
    print('')
