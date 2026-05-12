'''
*--------------------------------------------------------*
 * Fatec São Caetano do Sul *
 * Atividade B2-3 *
 * Autor: Enzo Schiavo *
*--------------------------------------------------------*
'''

def analisar_arvore(self):
    print("Analisando árvore...\n")
    node = self.raiz
    print(f"Profundidade do nó: {self.calcular_profundidade(node.valor)}")
    print(f"Altura do nó: {self.calcular_altura(node)}")
    print(f"Id do nó: {id(node)}")
    print(f"{node.valor} - Raiz\n")
    self.imprimir_descendentes(valor_busca)

def imprimir_nos_internos(self):
    def lookFor (raiz):
        l = raiz.esq is not None
        r = raiz.dir is not None

        if raiz != self.raiz and (l or r):
            print(f"{raiz.valor}")
                
        if l:
            lookFor(raiz.esq)
            
        if r:
            lookFor(raiz.dir)
    lookFor(self.raiz)
            
def imprimir_folhas(self):
    def lookFor (raiz):
        if raiz.esq is not None:
            lookFor(raiz.esq)
        elif raiz.dir is None:
            print(f"folha - {raiz.valor}")
            return

        if raiz.dir is not None:
            lookFor(raiz.dir)
        elif raiz.esq is None:
            print(f"folha - {raiz.valor}")
            return
    lookFor(self.raiz)
        

def imprimir_niveis(self):
    print(f"raiz - {self.raiz.valor} - Nível 1")
    niveis = []
    def lookFor(rt, nivel):
        n = nivel
        if rt.esq:
            niveis.append({"h" : n + 1, "node": rt.esq})
            lookFor(rt.esq, n + 1)
            
        if rt.dir:
            niveis.append({"h" : n + 1, "node": rt.dir})
            lookFor(rt.dir, n + 1)
                
    lookFor(self.raiz, 0)   
    niveis.sort(key = lambda x: x["h"])
    i = 0
    while i < len(niveis):
        print(f"{niveis[i]["node"].valor} - nível {niveis[i]["h"]}")
        i += 1

def calcular_altura(self, no):
    if no is None:
        return 0
    else:
        l = self.calcular_altura(no.esq)
        r = self.calcular_altura(no.dir)
        return 1 + max(l, r)
            
            
def calcular_profundidade(self, valor):
    def lookFor(no, p):
        if no is None:
            return -1

        if no.valor == valor:
            return p
        l = lookFor(no.esq, p + 1)
        if l != -1:
            return l

        r = lookFor(no.dir, p + 1)
        return r
    return lookFor(self.raiz, 0)
        
def imprimir_ancestrais(self, valor):
    if valor != self.raiz.valor:
        print("Imprimindo ancestrais")
    niveis = []
    def lookFor(no):
        if no is None:
            if no == self.raiz:
                print("Lista vazia.")
            return False
            
        if no.valor == valor:
            return True
            
        if lookFor(no.esq) or lookFor(no.dir):
            niveis.append(f"{no.valor}")
            return True
            
        return False

    if not lookFor(self.raiz):
        print("Valor não encontrado")
    else:
        i = len(niveis) - 1 
        while i >= 0:
            print(f"{niveis[i]}")
            i -= 1

        
def imprimir_descendentes(self, valor):
    if valor == self.raiz.valor:
        print("Imprimindo descendentes da Árvore")
    else:
        print("Imprimindo descententes")
    def lookFor(no, l):
        if no is None:
            if no == self.raiz:
                print("Lista vazia.")
            l = 0
            return

        if no.valor != valor:
            if l == 1:
                print(no.valor)
        else:
            l = 1

        lookFor(no.esq, l)
        lookFor(no.dir, l)
        return
    lookFor(self.raiz, 0)