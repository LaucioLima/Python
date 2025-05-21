class Tabuada:
    def __init__(self, numero):
        self.valor = numero
        self._resultado = 0 
        
    def soma(self):
        for i in range(1, 11):
            self._resultado = self.valor + i
            print(f"{self.valor} + {i} = {self._resultado}")
    
    def subtracao(self):
        for i in range(1, 11):
            self._resultado = self.valor - i
            print(f"{self.valor} - {i} = {self._resultado}")
    
    def multiplicacao(self):
        for i in range(1, 11):
            self._resultado = self.valor * i
            print(f"{self.valor} * {i} = {self._resultado}")    

    def divisao(self):
        for i in range(1, 11):
            self._resultado = self.valor / i
            print(f"{self.valor} / {i} = {self._resultado:.2f}")


numero = int(input("Digite um número: "))
tabuada = Tabuada(numero)

print("\nTabuada de Soma:")
tabuada.soma()

print("\nTabuada de Subtração:")
tabuada.subtracao()

print("\nTabuada de Multiplicação:")
tabuada.multiplicacao()

print("\nTabuada de Divisão:")
tabuada.divisao()
