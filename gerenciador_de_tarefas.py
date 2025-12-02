import os

def limpar_tela():
    os.system('cls')

def adicionar_tarefa(lista_tarefas):
    nova_tarefa = input('Digite a tarefa a ser adicionada: ').strip()
    if nova_tarefa:
        lista_tarefas.append(nova_tarefa)
        print(f'Tarefa "{nova_tarefa}" adicionada com sucesso!')
    else:
        print('Erro: Você não pode adicionar uma tarefa vazia.')

def visualizar_tarefas(lista_tarefas):
    print('\n---SUAS TAREFAS---')
    if not lista_tarefas:
        print('Nenhuma tarefa cadastrada.')
    else:
        for numero, tarefa in enumerate(lista_tarefas, 1):
            print(f'{numero}. {tarefa}')

def remover_tarefa(lista_tarefas):
    visualizar_tarefas(lista_tarefas)
    if not lista_tarefas:
        return
    
    try:
        numero_escolhido = int(input('\nDigite o NÚMERO da tarefa para remover: '))
        indice_real = numero_escolhido - 1

        if 0 <= indice_real < len(lista_tarefas):
            tarefa_removida = lista_tarefas.pop(indice_real)
            print(f'Tarefa "{tarefa_removida}" removida com sucesso!')
        else:
            print('Erro: Esse número de tarefa não existe.')
    except ValueError:
        print('Erro: Digite apenas números inteiros.')

tarefas = []

while True:
    limpar_tela()
    print('=== GERENCIADOR DE TAREFAS ===')
    print('1. Adicionar tarefa')
    print('2. Visualizar tarefas')
    print('3. Remover tarefa')
    print('4. Sair')

    opcao = input('\nEscolha uma opção: ')

    match opcao:
        case '1':
            adicionar_tarefa(tarefas)

        case '2':
            visualizar_tarefas(tarefas)

        case '3':
            remover_tarefa(tarefas)

        case '4':
            print('Saindo... Até logo!')

        case _:
            print('Opção inválida!')

    if opcao != '4':
        input('\nPressione Enter para continuar...')





