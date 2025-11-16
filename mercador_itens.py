import itens
import random

itens_andar1 = [itens.armadura_leve, itens.cajado_de_madeira, itens.espetinho_de_rato]
itens_andar2 = []
itens_andar3 = []
# ---------- RANDOM DE ITENS ----------
def mercador_ambulante():
    return random.sample(itens_andar1, 3)

# ---------- MERCADOR COM ITENS ----------
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



