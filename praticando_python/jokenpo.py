import os
import random

def limpar_tela():
    os.system('cls')

def jogar_jokenpo():
    regras_vitoria = {
        "pedra": "tesoura",
        "tesoura": "papel",
        "papel": "pedra"
    }

    opcoes_validas = list(regras_vitoria.keys())

    while True:
        limpar_tela()
        print('--- JOKENPÔ SUPREMO ---')
        print('')

        computador = random.choice(opcoes_validas)

        usuario = input('Escolha (Pedra, Papel, tesoura) ou "sair": ').lower().strip()

        if usuario == 'sair':
            print('Obrigado por jogar!')
            break
        if usuario not in opcoes_validas:
            print('Opção inválida! tente novamente.')
            input('Pressione Enter para continuar...')
            continue
        print(f'\n Computador escolheu: {computador.upper()}')
        print(f'você escolheu: {usuario.upper()}')
        print('-' * 30)

        if usuario == computador:
            print('EMPATE!')
        
        elif regras_vitoria[usuario] == computador:
            print('VOCÊ VENCEU!')
        else:
            print('VOCÊ PERDEU!')
        
        input('\nPressione Enter para jogar novamente...')

jogar_jokenpo()
