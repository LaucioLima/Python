#Calcuadora
#Obs - Este código tem um erro na divisão
def calculadora(valor_um,valor_dois,operador):
    if operador == "+":
        resultado = valor_um + valor_dois
        return resultado
    elif operador == "-":
        resultado = valor_um - valor_dois
        return resultado
    elif operador == "*":
        resultado = valor_um * valor_dois
        return resultado
    elif operador == "/":
        resultado = valor_um / valor_dois
        return resultado
    else:
        resultado = "Operação inválida"
        return resultado
    

#Programação
valor_um = int(input("Informe o primeiro valor: "))
operador = input("Informe a operação: (+,-,*,/)")
valor_dois = int(input("Informe o segundo Valor: "))

if operador == "/" and valor_dois == 0:
    print("Erro: Divisão por zero não é permitida")
else:
    print(calculadora(valor_um,valor_dois,operador))