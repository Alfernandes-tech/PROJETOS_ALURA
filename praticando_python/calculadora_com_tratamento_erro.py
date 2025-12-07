import os

os.system('cls')

print('Seja bem vindo a calculadora de entradas')

def soma(a, b):
    return a + b
def subtracao(a, b):
    return a - b
def multiplicacao(a, b):
    return a * b
def divisao(a, b):
    return a / b

while True:

    print('\n Para encerrar digite "sair" a qualquer momento.')

    entrada_1 = input('Digite o primeiro número: ').lower()
    if entrada_1 == 'sair':
        print('Encerrando calculadora...')
        break

    operacao_escolhida = input('Escolha a operação (+, -, *, /): ').lower()
    if operacao_escolhida == 'sair':
        break

    entrada_2 = input('Digite o segundo número: ').lower()
    if entrada_2 == 'sair':
        break


    try:

        primeiro_numero = float(entrada_1)
        segundo_numero = float(entrada_2)

        if operacao_escolhida == '+':
            resultado = soma(primeiro_numero, segundo_numero)
            print(f'Resultado: {resultado}')

        elif operacao_escolhida == '-':
            resultado = subtracao(primeiro_numero, segundo_numero)
            print(f'Resultado: {resultado}')

        elif operacao_escolhida == '*':
            resultado = multiplicacao(primeiro_numero, segundo_numero)
            print(f'Resultado: {resultado}')

        elif operacao_escolhida == '/':
            resultado = divisao(primeiro_numero, segundo_numero)
            print(f'Resultado: {resultado}')
        
        else:
            print('Opção inválida de operação.')
        
    except ValueError:
        print(f'Erro: Entrada inválida. Digite apenas números.')

    except ZeroDivisionError:
        print('Erro: Divisão por zero não é permitida.')
