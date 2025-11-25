import os
import random

os.system('cls')

def gerar_numero_aleatorio():
    numero_aleatorio = random.randint(1, 100)
    return numero_aleatorio


print('Vamos começar o jogo da advinhação')

numero_aleatorio = gerar_numero_aleatorio()

while True:
    try:
        escolha_jogador = int(input('Tente advinhar o número (1-100): '))

        if escolha_jogador < 1 or escolha_jogador > 100:
            print('Entrada inválida: Numero fora do intervalo! Digite um numero entre 1 e 100')
            continue

        if escolha_jogador == numero_aleatorio:
            print(f'Parabéns! Você acertou o número: {numero_aleatorio}')
            break

        elif escolha_jogador < numero_aleatorio:
            print('Esta baixo! Tente novamente.')

        elif escolha_jogador > numero_aleatorio:
            print('Esta alto! Tente novamente.')

    except ValueError as e:
        print(f'Entrada inválida: Você digitou um valor inválido: {e}')

print('Fim de jogo!')