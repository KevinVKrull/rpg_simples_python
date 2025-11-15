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

def tesouro(mago_do_tempo):
    item = bau_de_madeira()
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