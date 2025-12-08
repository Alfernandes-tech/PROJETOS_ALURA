import os

def limpar_tela():
    os.system('cls')

limpar_tela()

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f' {self.nome} | {self.categoria}'
    
    def listar_restaurante():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')


restaurante_praca = Restaurante('Bistrô', 'Fast Food')

restaurante_pizza = Restaurante('Pizza Express', 'Pizzaria')


Restaurante.listar_restaurante()

