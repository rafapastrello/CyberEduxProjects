# PASTRELLO 

import sqlite3

""" Cria uma conexão com o banco de dados """
conexao_db = sqlite3.connect('DB_Rent_A_Car.db')

""" Cria um cursor para executar comandos SQL """
cursor = conexao_db.cursor()

def cadastro_veiculos():
    """
    - Função responsável por cadastrar os veículos de uma locadora de veículos;
    - O usuário pode escolher entre as seguintes opções:
    v. Para voltar ao menu principal.
    1. Cadastrar veículo - Para adicionar um veícuulo à tabela 'veiculos'.
    2. Editar dados do veículo por ID - Para editar alguma informação do veículo.
    3. Excluir veículo por ID - Para excuir um veículo da tabela.
    - A função entra em um loop, exibindo o menu e aguardando a entrada do usuário;
    - Com base na escolha do usuário, a função direciona para a função correspondente;
    - Não são necessários argumentos de entrada para esta função.
    - Exemplo de uso:
    >>> cadastro_veiculos()
    """

    def menu_veiculo():
        """
        - Função para exibir o menu principal do arquivo, que possui as opções: [v] Voltar ao menu principal, 
        [1] Cadastrar veículo, [2] Editar dados do veículo por ID, [3] Excluir veículo por ID,
        - Não recebe parâmetros;
        - Exemplo de uso:
        >>> menu_veiculo():
        """

        while True:
            opcao = input("""
    *********************************************************
        _____________________ OPÇÕES ____________________

        [v] .................... Voltar ao menu principal
        [1] ........................... Cadastrar veículo
        [2] .............. Editar dados do veículo por ID
        [3] ...................... Excluir veículo por ID
    *********************************************************

    >>> Digite a opção: """)
            if opcao == 'v':
                print('\n - VOLTANDO AO MENU PRINCIPAL!!! - \n')
                break
            elif opcao == '1':
                print('\n - CADASTRAR VEÍCULO - \n')
                cadastrar_veiculo()
            elif opcao == '2':
                print('\n - EDITAR DADOS DO VEÍCULO POR ID - \n')
                editar_veiculo()
            elif opcao == '3':
                print('\n - EXCLUIR VEÍCULO POR ID - \n')
                excluir_veiculo()
            else:
                print(f'\n - OPÇÃO > {opcao} < INVÁLIDA!!! - \n')

    def cadastrar_veiculo():
        """
        - Função para inserir veículo na tabela 'veiculos';
        - Não recebe parâmetros;
        - Exemplo de uso:
        >>> cadastrar_veiculo():
        """
        fabricante_veiculo = input("Digite o fabricante do veículo: ")
        modelo_veiculo = input("Digite o modelo do veículo: ")
        ano_veiculo = input("Digite o ano do veículo: ")
        cor_veiculo = input("digite a cor do veículo: ")
        valor_diaria_veiculo = input("Digite o valor da diária do veículo: ")

        cursor.execute ('''
                            INSERT INTO veiculos VALUES (null, ?, ?, ?, ?, ?)
                        ''', (fabricante_veiculo, modelo_veiculo, ano_veiculo, cor_veiculo, valor_diaria_veiculo))
        conexao_db.commit()

        print(f'\n - VEÍCULO > {modelo_veiculo} < CADASTRADO!!! - \n')

    def editar_veiculo():
        """
        - Função para editar os dados do veículo, buscando-o pela chave(id_veiculo) na tabela 'veiculos' e permitindo alterar o fabricante, o modelo, o ano, a cor e o valor da diária do veículo;
        - Não recebe parâmetros;
        - Exemplo de uso:
        >>> editar_veiculo():
        """
        ID_veiculo = input('ID(veículo): ')
        cursor.execute (''' SELECT *
                            FROM veiculos
                            WHERE id_veiculo = ?
                        ''', (ID_veiculo,))
        resultado = cursor.fetchone()
        if resultado:
            opcao = input("""
            **********************************************************
                _____________________ OPÇÕES _____________________

                [v] ....................................... Voltar
                [1] ................ Alterar fabricante do veículo
                [2] .................... Alterar modelo do veículo
                [3] ....................... Alterar ano do veículo
                [4] ..................... Alterar a cor do veículo
                [5] ......... Alterar o valor da diária do veículo
            **********************************************************

            >>> Digite a opção: """)

            if opcao == 'v':
                print('\n - VOLTANDO!!! - \n')
                return
            elif opcao == '1':
                novo_fabricante_veiculo = input("Digite o novo fabricante do veículo: ")
                cursor.execute (''' UPDATE veiculos
                                    SET fabricante_veiculo = ?
                                    WHERE id_veiculo = ?
                                ''', (novo_fabricante_veiculo, ID_veiculo))
                print('\n - ALTERAÇÃO CONCLUÍDA!!! - \n')
            elif opcao == '2':
                novo_modelo_veiculo = input("Digite o novo modelo do veículo: ")
                cursor.execute (''' UPDATE veiculos
                                    SET modelo_veiculo = ?
                                    WHERE id_veiculo = ?
                                ''', (novo_modelo_veiculo, ID_veiculo))
                conexao_db.commit()
                print('\n - ALTERAÇÃO CONCLUÍDA!!! - \n')
            elif opcao == '3':
                novo_ano_veiculo = input("Digite o novo ano do veículo: ")
                cursor.execute (''' UPDATE veiculos
                                    SET ano_veiculo = ?
                                    WHERE id_veiculo = ?
                                ''', (novo_ano_veiculo, ID_veiculo))
                conexao_db.commit()
                print('\n - ALTERAÇÃO CONCLUÍDA!!! - \n')
            elif opcao == '4':
                nova_cor_veiculo = input("digite a nova cor do veículo: ")
                cursor.execute (''' UPDATE veiculos
                                    SET cor_veiculo = ?
                                    WHERE id_veiculo = ?
                                ''', (nova_cor_veiculo, ID_veiculo))
                conexao_db.commit()
                print('\n - ALTERAÇÃO CONCLUÍDA!!! - \n')
            elif opcao == '5':
                novo_valor_veiculo = input("Digite o novo valor da diária do veículo: ")
                cursor.execute (''' UPDATE veiculos
                                    SET valor_diaria_veiculo = ?
                                    WHERE id_veiculo = ?
                                ''', (novo_valor_veiculo, ID_veiculo))
                conexao_db.commit()
                print('\n - ALTERAÇÃO CONCLUÍDA!!! - \n')
        else:
            print(f'\n - ID {ID_veiculo} INEXISTENTE!!! - \n')

    def excluir_veiculo():
        ID_veiculo = input("ID(veículo):")
        cursor.execute (''' DELETE FROM veiculos
                            WHERE id_veiculo = ?
                        ''',(ID_veiculo,))
        conexao_db.commit()
        print(f'\n - VEÍCULO {ID_veiculo} EXCLUÍDO!!! - \n')

    menu_veiculo()

if __name__ == '__main__':
    cadastro_veiculos()
