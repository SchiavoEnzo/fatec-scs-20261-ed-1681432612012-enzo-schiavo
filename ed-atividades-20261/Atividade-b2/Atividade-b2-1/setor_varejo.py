import random

fila1 = []
fila2 = []

itens = [
    "Camiseta Polo",
    "Calça Jeans",
    "Tênis Esportivo",
    "Jaqueta Bomber",
    "Meia Cano Longo",
    "Boné Aba Curva",
    "Shorts Tactel",
    "Vestido Floral",
    "Camisa Social",
    "Moletom Canguru",
]

def inserir_pedido(id_pedido, nome_item, quantidade_pecas):
    pedido = {
        "id_pedido": id_pedido,
        "nome_item": nome_item,
        "quantidade_pecas": quantidade_pecas
    }
    fila1.append(pedido)
    print("ID: " + str(id_pedido) + ", Item: " + nome_item + ", Qtd: " + str(quantidade_pecas) + " peças")

def mostrar_fila1():
    print("\nFila 1 - Pedidos Pendentes:")
    if len(fila1) == 0:
        print("  (fila vazia)")
    for pedido in fila1:
        print("  ID: " + str(pedido["id_pedido"]) + ", Item: " + pedido["nome_item"] + ", Qtd: " + str(pedido["quantidade_pecas"]) + " peças")

def mostrar_fila2():
    print("\nFila 2 - Lotes Consolidados:")
    if len(fila2) == 0:
        print("  (fila vazia)")
    for lote in fila2:
        print("  Lote: " + str(lote["ids_pedidos"]) + " | Total: " + str(lote["total_pecas"]) + " peças | Prioridade: " + lote["prioridade"])

def processar_lotes():
    numero_lote = 1

    while len(fila1) > 0:
        pedidos_do_lote = []
        total = 0
        ids = []

        while len(fila1) > 0:
            proximo = fila1[0]
            total = total + proximo["quantidade_pecas"]
            pedidos_do_lote.append(fila1.pop(0))
            ids.append(proximo["id_pedido"])

            if total > 50:
                break

        if total > 50:
            prioridade = "Alta (Carga Fechada)"
        else:
            prioridade = "Normal"

        lote = {
            "numero_lote": numero_lote,
            "ids_pedidos": ids,
            "total_pecas": total,
            "prioridade": prioridade
        }

        fila2.append(lote)
        print("  Lote " + str(numero_lote) + " criado -> IDs: " + str(ids) + " | Total: " + str(total) + " peças | Prioridade: " + prioridade)

        numero_lote = numero_lote + 1


print("=== GERANDO PEDIDOS NA FILA 1 ===")

id_atual = 701

for i in range(8):
    nome = random.choice(itens)
    quantidade = random.randint(5, 40)
    inserir_pedido(id_atual, nome, quantidade)
    id_atual = id_atual + 1

mostrar_fila1()

print("\n=== PROCESSANDO LOTES ===")
processar_lotes()

mostrar_fila1()
mostrar_fila2()