import itens
import random

itens_andar1 = [itens.espada_quebrada, itens.amuleto_quebrado, itens.amuleto_de_regeneracao, itens.cajado_do_tempo, itens.espetinho_de_rato, itens.amuleto_de_velocidade]


def mercador_ambulante():
    return random.sample(itens_andar1, 3)




