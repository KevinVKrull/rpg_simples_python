import itens
import random


def bau_de_madeira():
    lista_itens = [itens.amuleto_quebrado, itens.espada_quebrada, itens.cajado_de_madeira, itens.espetinho_de_rato]
    chance = [10, 10, 10, 2]

    item = random.choices(lista_itens, weights=chance)[0]

    return item

def bau_de_prata():

    lista_itens = [itens.armadura_leve, itens.espada_quebrada, itens.cajado_de_madeira, itens.espetinho_de_rato]
    chance = [10, 10, 10, 2]

    item = random.choices(lista_itens, weights=chance)[0]

    return item

def bau_de_ouro():

    lista_itens = [itens.armadura_pesada, itens.cajado_do_tempo, itens.amuleto_de_regeneracao, itens.amuleto_de_velocidade]
    chance = [10, 10, 10, 2]

    item = random.choices(lista_itens, weights=chance)[0]

    return item