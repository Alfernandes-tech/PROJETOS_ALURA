import os
import random
import string

os.system('cls')

def gerar_senha():
    maiusculas = string.ascii_uppercase
    minusculas = string.ascii_lowercase
    numeros = string.digits
    especiais = "!@#$%¨&*"

    senha_lista = [
        random.choice(maiusculas),
        random.choice(minusculas),
        random.choice(numeros),
        random.choice(especiais)
    ]
    todos_caracteres = maiusculas + minusculas + numeros + especiais
    complemento = random.choices (todos_caracteres, k=8)

    senha_lista.extend(complemento)

    random.shuffle(senha_lista)

    return ''.join(senha_lista)

print('Seja bem vindo ao gerador de senhas seguras')

escolha = input('Você gostaria de gerar a senha? Digite "sim" para continuar ou "não" para sair').lower().strip()

match escolha:
    case "sim" | "s":
        senha_final = gerar_senha()
        print(f'\n Sua nova senha segura é: {senha_final}')
    case "não" | "nao" | "n":
        print('\n Tudo bem! Até a próxima.')
    case _:
        print('\n Opção inválida. Por favor reinicie e digite "sim" ou "não".')
