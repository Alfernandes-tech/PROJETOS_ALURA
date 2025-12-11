import os

def limpar_tela():
     os.system('cls')

class Carro:
    carros = []

    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        Carro.carros.append(self)

    def __str__(self):
            return f' Modelo: {self.modelo} | Cor: {self.cor} | Ano: {self.ano}'

    @staticmethod    
    def listar_carros():
            for carro in Carro.carros:
                print (carro)



class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria, capacidade, nota, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.capacidade = capacidade
        self.nota = nota
        Restaurante.restaurantes.append(self)

    def __str__(self):
            status = 'Ativo' if self.ativo else 'Inativo'
            return f' Nome: {self.nome} | Categoria: {self.categoria} | Capacidade: {self.capacidade} | Nota: {self.nota} | Status: {status}'

    @staticmethod    
    def listar_restaurantes():
            for restaurante in Restaurante.restaurantes:
                print (restaurante)

class Cliente:
    clientes = []
    def __init__(self, nome, idade, email, telefone):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone
        Cliente.clientes.append(self)

    def __str__(self):
        return f'Cliente: {self.nome} | Email: {self.email}'
    
    @staticmethod
    def listar_clientes():
         for cliente in Cliente.clientes:
              print(cliente)



#Área para criação de atributos


#Objetos "Carro"
carro_c4 = Carro('C4 Lounge', 'Branco', '2015')
carro_picasso = Carro('Xsara Picasso', 'Prata', '2008')

#Objetos "Restaurante"
restaurante_Batataria = Restaurante('Batatas da Val', 'Batataria', 50, 4.5)
restaurante_confeitaria = Restaurante('Valzinha confeiteira', 'Confeitaria', 20, 5.0, True)

#Objetos "Cliente"
cliente_cliente1 = Cliente("Miguel", 25, "miguel@email.com", "1199999-9999")
cliente_cliente2 = Cliente("Ana", 30, "ana@email.com", "2198888-8888")
cliente_cliente3 = Cliente("Carlos", 45, "carlos@email.com", "3197777-7777")


#Saídas para o terminal

limpar_tela()

print('---Lista de Carros---')
Carro.listar_carros()

print("\n--- Lista de Restaurantes ---")
Restaurante.listar_restaurantes()

print("\n--- Clientes ---")
Cliente.listar_clientes()
