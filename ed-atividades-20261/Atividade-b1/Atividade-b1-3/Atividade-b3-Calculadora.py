operador = 0
class Pilha:
    
    def __init__ (self):
        self.itens = []
        self.next = 0
        
    def add(self, number):
        if len(self.itens) < 4:
            self.itens.append(number)
        else: 
            for i in range(4):
                if i < 3:
                    self.itens[i] = self.itens[i + 1]
                else:
                    self.itens[3] = number
        list() 
        print("\n-----------\nAdicionaddo\n-----------")
        
    def operate (self, option):
        res = 0
        if operador > 0:
            j = len(self.itens)
            for i in reversed(self.itens):
                if self.nextO < j :
                    if option == "+":
                        res += i
                    elif option == "-":
                        res -= i
                    elif option == "/":
                        res /= i
                    elif option == "*":    
                        res *= i
                else:    
                    break
                j -= 1
            self.itens[-2] = res
            self.nextO = self.itens.index(self.itens[-2], -3)
            self.itens.pop()
        elif len(self.itens) > 1:
            for i in self.itens:
                if option == "+":
                    res += i
                elif option == "-":
                    res -= i
                elif option == "/":
                    res /= i
                elif option == "*":    
                    res *= i
            self.itens[-2] = res
            self.nextO = self.itens.index(self.itens[-2], -3)
            self.itens.pop()
        else:
            self.itens[-1] = self.itens[-1] + self.itens[-2]
        print(str(self.itens[-1]))
    
   
    
    def list(self):
        j = 0
        if len(self.itens) == 0 :
            print("Lista vazia")
            return
        print("\nmostrando\n")
        for i in self.itens:
            if self.itens[j] :
                print(str(self.itens[j]) + "\n")
            else: 
                break
            j += 1
        
def is_number(s):
    try:
        float(s)
        return True
    except error:
        return False

pilha = Pilha()
while True:
    
    option = input("Input: \n")
    if option == "+" or option == "-" or option == "/" or option == "*":
        pilha.operate(option)
        operador += 1
    elif option == "listar":
        pilha.list()
    elif option == "cls":
        pilha.itens.clear()
        operador = 0
        print("Limpo")
    elif is_number(option):
        pilha.add(float(option))
    elif option == "break":
        break