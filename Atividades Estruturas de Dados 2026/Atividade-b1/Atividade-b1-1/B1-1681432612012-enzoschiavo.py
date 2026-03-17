'''
    *---------------------------------------------------------*
    * Fatec São Caetano do Sul *
    * Atividade B1-1 *
    * Autor: 11111111111 - nome *
    * Objetivo:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx *
    * data: 24/02/2026 *
    *---------------------------------------------------------*
'''

catalogo = {}

def adicionar_filme(id_filme, titulo, diretor): 
    if id_filme not in catalogo:
        catalogo[id_filme] = {"titulo": titulo, "diretor": diretor}
        
def buscar_filme(id_filme):
    if id_filme in catalogo:
        return catalogo.get(id_filme)
    else:
        return null
        
def remover_filme(id_filme):
    if id_filme in catalogo:
        catalogo.pop(id_filme)

def listar_todos():
    if not catalogo:
        print("\n O catálogo está vazio")
    else:
        print("\n  --- Listagem de Filmes --- ")
        for idf, dat in catalogo.items():
            print("Id: " + idf + " | Título: " + dat['titulo'] + " | Diretor: "+ dat['diretor'] )      