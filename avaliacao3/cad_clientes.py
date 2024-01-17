# ISIS

import sqlite3
conexao= sqlite3.connect('DB_Rent_A_Car.db')

sql = conexao.cursor()

sql.execute('''



    ''')





def cadastro_clientes():


    #  função para cadastrar clientes
    def cadastrarClientes():
        while True :  

            nome_cliente = input("Digite o nome do cliente: ")
            cpf_cliente = input("Digite o CPF do cliente: ")
            habilitacao_cliente = input("Categoria da CNH do cliente: ")
            data_nascimento_cliente = input('Digite a data de nascimento: ')
            endereco_cliente = input("Digite o endereço: ")
            telefone_cliente = input("Digite o telefone: ")
            email_cliente =  input("Digite o email: ")


            sql.execute('''
                INSERT INTO clientes (id_cliente,nome_cliente,cpf_cliente,habilitacao_cliente,data_nascimento_cliente,endereco_cliente, telefone_cliente,email_cliente) values (null,?,?,?,?,?,?,?)
                        ''',(nome_cliente,cpf_cliente,habilitacao_cliente,data_nascimento_cliente,endereco_cliente,telefone_cliente,email_cliente))
            conexao.commit()

            continuar = input(" Dejesa criar outro cliente(s/n):")

            while continuar != 's' and continuar != 'n':
                continuar = input("Coloque uma resposta válida:")

            if continuar == 'n':
                break    
    # função para editar cliente

    def EditarCliente():
        escolhaCodigo = input('Digite o código do cliente :')
        print('- 1-nome \n -2- cpf \n -3-habilitação \n - 4-telefone\n 5- email \n -6- endereço \n-7- data_nascimento')

        dicionario = {1:'nome_cliente',2:'cpf_cliente',3:'habilitacao_cliente',4:'telefone_cliente',5:'email_cliente',6:'endereco_cliente',7:'data_nascimento_cliente'}

        parte =int( input('qual parte do cliente:'))
        novoAtributo = input("Dejesa substituir esse atributo pelo o que:")

        # Construir a instrução SQL dinamicamente
        consulta_sql = f"UPDATE clientes SET {dicionario[parte]} = ? WHERE id_cliente = ?"

        # Executar a consulta

        sql.execute(consulta_sql, (novoAtributo, escolhaCodigo))
        print("Cliente editado")
        print("="*30)
        # Commit (confirmar as alterações)
        conexao.commit()


    # função para deletar
    def deletarCliente():
        dele = int(input("Insira o codigo que queira deletar:"))
        sql.execute( "DELETE FROM clientes  WHERE id_cliente = ?" ,(dele,) )
        print("Cliente deletado!")
        print("=" * 30)
        conexao.commit()


    # função para mostrar o menu
    def menuCliente(): 
        print("1- Cadastrar cliente")
        print("2- Editar cliente")
        print("3- Deletar cliente")
        print("4- Sair")

    # -------------------------------------

    while True:

        menuCliente()
        opcao = int(input('Escolha uma opção:'))

        if(opcao == 1):
            cadastrarClientes()

        elif opcao ==2 :
            EditarCliente()

        elif opcao == 3:
            deletarCliente()

        elif opcao == 4:
            print("Saindo....")
            break
if __name__ == '__main__':
    cadastro_clientes()