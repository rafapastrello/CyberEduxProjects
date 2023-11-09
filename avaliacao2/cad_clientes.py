# ISIS

#clientes 

import json
import os

def cadastrar_clientes():

    # função para salvar cliente
    def salvarCliente(clientes):
        with open("clientes.txt",'w') as c:
            json.dump(clientes,c) 

    # função para carregar
    def carregarCliente():
        if not os.path.exists('clientes.txt'):
            salvarCliente({})
        with open('clientes.txt','r') as r:
            cliente = json.loads(r.read())
            return cliente
            
    #  função para cadastrar clientes
    def cadastrarClientes(clientes):
        while True :     
            nome = input("Digite o nome do cliente:")
            CPF = input("Digite o CPF do cliente:")
            habilitacao= input("O cliente possui habilitação:")
            endereco = input("Digite o endereço:")
            telefone=input("digite o telefone:")
            email=input("Digite o gmail:")
                
            if clientes == dict():
                codigo = 1
            else:
                codigo = max(int(key) for key in clientes.keys()) + 1

        
            clientes[codigo] = nome,CPF,habilitacao,telefone,email,endereco 

            continuar = input(" Dejesa criar outro cliente(s/n):")

            while continuar != 's' and continuar != 'n':
                continuar = input("Coloque uma resposta válida:")
            
            if continuar == 'n':
                break

    # visualizar clientes 

    def visualizarClientes(clientes): 
        print('')
        print(f'{"código":<6} | {"nome":<15} | {"CPF":<17} | {"habilitação":<13} | {"telefone":<15} | {"gmail":<17} | {"endereço":<13}')
        print("-" * 120)
        for i in clientes.keys():
            print(f'{i:<6} | {clientes[i][0]:<15} | {clientes[i][1]:<17} | {clientes [i][2]:<13} | {clientes [i][3]:<15} | {clientes [i][4]:<18}| {clientes [i][5]:<13}')
        print('')
    
    # função para editar cliente

    def EditarCliente(cliente):
        escolhaCodigo = input('Digite o código do cliente :')
        print('1- nome \n 2- cpf \n 3-habilitação \n 4-telefone\n 5-email \n 6-endereço')

        parte = int(input('qual parte do cliente:'))
        novoAtributo = input("Dejesa substituir esse atributo pelo o que:")
        if escolhaCodigo in cliente:
            print( cliente[escolhaCodigo][parte -1] )
            cliente[escolhaCodigo][parte -1] = novoAtributo
        else:
            print("Esse codigo não existe")

    # função para deletar
    def deletarCliente(cliente):
        escolha = input("Insira o codigo que queira deletar:")
        deletar = cliente.pop(escolha)
        print("Cliente deletado!")
        return deletar
        
    # função para mostrar o menu
    def menuCliente(): 
        print("1- cadastrar cliente")
        print("2-visualisar cliente")
        print("3-Editar cliente")
        print("4-Deletar cliente")
        print("5-sair")

    # -------------------------------------

    while True:
        clientes = carregarCliente()
        menuCliente()
        opcao = int(input('Escolha uma opção:'))

        if(opcao == 1):
            cadastrarClientes(clientes)
            salvarCliente(clientes)

        elif opcao ==2 :
            visualizarClientes(clientes)

        elif opcao ==3 :
            EditarCliente(clientes)
            salvarCliente(clientes)
        elif opcao == 4:
            deletarCliente(clientes)
            salvarCliente(clientes)
        elif opcao == 5:
            print("Saindo....")
            break
if __name__ == '__main__':
    cadastrar_clientes()

