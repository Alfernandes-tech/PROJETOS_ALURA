import os

def limpar_tela():
    os.system('cls')

limpar_tela()

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        status = 'Ativo' if self.ativo else 'Inativo'
        return f'{self.nome.ljust(20)} | {self.categoria.ljust(20)} | {status}'
    
    def listar_restaurante():
        print(f'{'Nome do Restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | Status')
        print('-' * 70)
        for restaurante in Restaurante.restaurantes:
            print(restaurante)

    @property
    def ativo(self):
        return 'Ativo' if self._ativo else 'Desativado'



restaurante_praca = Restaurante('Bistrô', 'Fast Food')

restaurante_pizza = Restaurante('Pizza Express', 'Pizzaria')


Restaurante.listar_restaurante()

