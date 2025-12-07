import os

def limpar_tela():
    os.system('cls')

def sacar_dinheiro(valor_saque):
    cedulas_disponiveis = [100, 50, 20, 10, 5, 2]
    
    print(f"\n--- Sacando R$ {valor_saque} ---")
    
    for cedula in cedulas_disponiveis:
        quantidade_notas = valor_saque // cedula
        
        if quantidade_notas > 0:
            print(f"{quantidade_notas} cédula(s) de R$ {cedula}")
            
            valor_saque = valor_saque % cedula
            
    if valor_saque > 0:
        print(f"Sobrou R$ {valor_saque} que não pode ser sacado (sem cédulas disponíveis).")

while True:
    limpar_tela()
    print("=== CAIXA ELETRÔNICO PYTHON ===")
    print("Notas disponíveis: 100, 50, 20, 10, 5, 2")
    
    print("\nDigite 'sair' para encerrar.")
    entrada = input("Digite o valor do saque: ").lower().strip()

    if entrada == 'sair':
        print("Encerrando sistema... Obrigado!")
        break

    try:
        valor = int(entrada)

        if valor <= 0:
            print("❌ Erro: O valor deve ser positivo.")
        
        elif valor % 2 != 0:
            print("❌ Erro: O caixa não possui moedas de R$ 1. Digite um valor par.") # Nota abaixo*
            
        else:
            sacar_dinheiro(valor)

    except ValueError:
        print("❌ Erro: Digite apenas números inteiros válidos.")

    input("\nPressione Enter para realizar um novo saque...")