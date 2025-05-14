nome = input("Informe o nome do titular: ")

nome_titular = (nome,)

valor_deposito = float(input("Informe o valor do depósito: "))

saldo = [valor_deposito]

historico = [f"Depósito inicial: R$ {valor_deposito:.2f}"]

print(f"\nBem-vindo, {nome_titular[0]}, seu saldo é de R$ {saldo[0]:.2f}.\n")


while True:
    print("\nComo podemos ajudar?")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Consultar Saldo")
    print("4. Consultar Histórico")
    print("5. Sair")

    opcao = input("Qual é a sua opção? ")

    if opcao == "1":
        try:
            deposito = float(input("Qual o valor do depósito? "))
            if deposito > 0:
                saldo[0] += deposito
                historico.append(f"Depósito: R$ {deposito:.2f}")
                print(f"Depósito realizado. Novo saldo: R$ {saldo[0]:.2f}")
            else:
                print("O valor deve ser positivo.")
        except ValueError:
            print("Digite um número válido.")

    elif opcao == "2":
        try:
            saque = float(input("Qual o valor de saque? "))
            if saque <= 0:
                print("O valor deve ser positivo.")
            elif saque > saldo[0]:
                print("Saldo insuficiente.")
            else:
                saldo[0] -= saque
                historico.append(f"Saque: R$ {saque:.2f}")
                print(f"Saque realizado. Saldo restante: R$ {saldo[0]:.2f}")
        except ValueError:
            print("Digite um número válido.")

    elif opcao == "3":
        print(f"Seu saldo atual é: R$ {saldo[0]:.2f}")

    elif opcao == "4":
        print("Histórico da conta:")
        for item in historico:
            print("-", item)

    elif opcao == "5":
        print("Operação finalizada! Até logo.")
        break

    else:
        print("Opção inválida. Tente novamente.")
