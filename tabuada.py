numero = int(input("Digite um número: "))

def multiplicar(numero):
    for i in range(1,11):
        print(f"{numero} x {i} = {numero * i}")
    
multiplicar(numero)    