import random


print("Escolha um nível de dificuldade:")
print("1. Fácil (30 tentativas)")
print("2. Médio (15 tentativas)")
print("3. Difícil (5 tentativas)")


dificuldade = int(input("Digite o número correspondente à dificuldade: "))


if dificuldade == 1:
    tentativas = 30
    perda_por_erro = 10
elif dificuldade == 2:
    tentativas = 15
    perda_por_erro = 20
elif dificuldade == 3:
    tentativas = 5
    perda_por_erro = 50
else:
    print("Opção inválida! Definido como Fácil.")
    tentativas = 30
    perda_por_erro = 10


pontos = 100

numero_secreto = random.randint(10, 100)

print(f"\nO jogo começou! Você tem {tentativas} tentativas.")
print(f"Número secreto está entre 10 e 100.")


for rodada in range(1, tentativas + 1):
    print(f"\nTentativa {rodada}/{tentativas}")
    while True:
        try:
            palpite = int(input("Digite seu palpite (entre 10 e 100): "))
            if 10 <= palpite <= 100:
                break
            else:
                print("O número precisa estar entre 10 e 100.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

    if palpite == numero_secreto:
        print(f"\nParabéns! Você acertou o número {numero_secreto}!")
        print(f"Sua pontuação final é: {pontos}")
        break
    elif palpite < numero_secreto:
        print("Muito baixo.")
    else:
        print("Muito alto.")

    
    pontos -= perda_por_erro
    print(f"Sua pontuação atual: {pontos}")
    print(f"Tentativas restantes: {tentativas - rodada}")


if palpite != numero_secreto:
    print(f"\nVocê perdeu! O número secreto era {numero_secreto}.")
    print(f"Sua pontuação final foi: {pontos}")
