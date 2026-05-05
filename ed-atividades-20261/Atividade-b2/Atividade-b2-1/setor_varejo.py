import random
fila1 = []

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

class Fila1:


    def inserir_pedido(self, id_pedido, nome_item, quantidade_pecas):
        pedido = {
            "id_pedido": id_pedido,
            "nome_item": nome_item,
            "quantidade_pecas": quantidade_pecas
        }
        fila1.append(pedido)
        print(f"ID: {id_pedido}, Item: {nome_item}, Qtd: {quantidade_pecas} peças")

    def mostrar_fila1(self):
        print("\nFila 1 - Pedidos Pendentes:")
        if len(fila1) == 0:
            print("  (fila vazia)")
        for pedido in fila1:
            print(f"  ID: {pedido["id_pedido"]}, Item: {pedido["nome_item"]}, Qtd: {pedido["quantidade_pecas"]} peças")
