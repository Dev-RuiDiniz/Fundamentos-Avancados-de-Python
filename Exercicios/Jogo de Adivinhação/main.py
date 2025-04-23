import random

numero_secreto = random.randint(1, 10)

print("Adivinhe o número entre 1 e 10. Você tem 3 tentativas!")

for tentativa in range(1, 4):
    entrada = input(f"Tentativa {tentativa}: ")

    if not entrada.isdigit():
        print("Digite um número válido!")
        continue  # Não conta a tentativa, mas vai pra próxima

    chute = int(entrada)

    if chute < 1 or chute > 10:
        print("O número deve estar entre 1 e 10.")
        continue

    if chute == numero_secreto:
        print("Parabéns! Você acertou.")
        break
    else:
        print("Errado!")

else:
    print(f"Suas tentativas acabaram! O número era {numero_secreto}.")
