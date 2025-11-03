import random
import os
import time

def apagar():
    if os.name == 'nt':  
        os.system('cls')
    else: 
        os.system('clear')

def escolha_acao():
    print('--------------- OPÇOES ---------------')
    print('')
    print('            Escolha sua ação:')
    print('1 -🌀 Rajada Temporal: (5 de mana, 10-15 Dano)')
    print('2 -⏳ Fenda do Tempo: (15 de mana 20-30 Dano)')
    print('3 -🔁 Ressurgir Temporal: (40 de mana, volta 2 turnos no tempo reverte histórico de status)')
    print('4 -🛡️  Defender: (50% redução de dano do próximo ataque do boss)')
    print('5 -❤️  Poção de Vida: (restaura de 20-30 de vida)')
    print('6 -🔮 Poção de Mana: (restaura de 25-35 de mana)')
    print('')

def texto():
    apagar()
    print('Após a derrota do Lorde Sombrio, Mago do Tempo descobre uma verdade perturbadora: ele era apenas um dos Cinco Lordes das Trevas. \n' \
    'No horizonte, uma torre mística emerge das sombras. \n' \
    'Seus cinco andares guardam segredos, perigos e tesouros. No topo, o próximo lorde o aguarda.')
    print('')
    print('-> Sua missão: escalar a Torre Sombria, sobreviver aos desafios de cada andar e derrotar o Senhor das Chamas no topo.') 

#-------------------- Texto continuar a torre --------------------
def continuar_para_torre1(andar):
    while True:
        continuar = input('Deseja Continuar para Torre 1? [S/N]: ').lower()

        if continuar == 's':
            andar += 1
            apagar()
            break
        else:
            andar = 0
            apagar()
            break
    return andar

#--------------------- GERADOR DE MAPA --------------------
def gerar_mapa():
    possiveis_salas = ['Combate','Tesouro','Mercador','Descanso','Evento']
    mapa = []

    for l in range(3):
        lista = []
        for c in range(3):
            if l == 0 and c == 0:
                lista.append('Inicio')
            elif l == 2 and c == 2:
                lista.append('Escadas')
            else:
                lista.append(random.choice(possiveis_salas))
        mapa.append(lista)
    return mapa

#--------------------- MAPA VISIVEL --------------------
def mapa_visivel():
    mapa_visivel = []
    for l in range(3):
        linha = []
        for c in range(3):
            linha.append('?')  # sala ainda não visitada
        mapa_visivel.append(linha)
    return mapa_visivel
