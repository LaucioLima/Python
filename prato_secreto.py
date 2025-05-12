import random   

pratos = ["Pizza", "Hamburguer", "Esfirra", "Sushi", "Açaí", "Sorvete", "Torta", "Bolo"]

tentativas = 5

pratos_deliciosos = random.choice(pratos)


while tentativas > 0:
    escolha_pratos = input("Digite um prato entre: Pizza, Hamburguer, Esfirra, Sushi, Açaí, Sorvete, Torta, Bolo ")

    if escolha_pratos not in pratos:
        print("Nome inválido! Digite um nome da lista.")
        continue
    if escolha_pratos == pratos_deliciosos:
        print("Parabéns! Você acertou!")
        break
    else:
        tentativas -= 1
        print(f"Errado, você ainda tem {tentativas} tentativa(s)")

if tentativas == 0:
    print(f"Suas tentativas acabaram. O nome correto era {pratos_deliciosos}")


