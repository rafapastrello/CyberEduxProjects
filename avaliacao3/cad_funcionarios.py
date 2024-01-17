# PASTRELLO

import sqlite3

# Cria uma conexão com o banco de dados
conexao_db = sqlite3.connect('DB_Rent_A_Car.db')

# Cria um cursor para executar comandos SQL
cursor = conexao_db.cursor()

def cadastro_funcionarios():
    """
    - Função responsável por cadastrar os funcionários de uma locadora de veículos;
    - O usuário pode escolher entre as seguintes opções:
    v. Para voltar ao menu principal.
    1. Cadastrar funcionárioS - Para adicionar um funcionário à lista.
    2. Excluir funcionário - Para excuir um funcionário da lista.
    3. Editar Funcionário - Para editar alguma informação do funcionário.
    - A função entra em um loop, exibindo o menu e aguardando a entrada do usuário;
    - Com base na escolha do usuário, a função direciona para a função correspondente;
    - Não recebe parâmetros;
    - Exemplo de uso:
    >>> cadastro_funcionarios()
    """

    def menu_funcionarios():
        """
        - Função para exibir o menu principal do arquivo, que possui as opções: [v] Voltar ao menu principal, [1] Cadastrar funcionários, [2] Editar dados do funcionário por ID, [3] Excluir funcionário por ID;
        - Não recebe parâmetros;
        - Exemplo de uso:
        >>> menu_funcionarios():
        """

        while True:
            opcao = input("""
    *********************************************************
        _____________________ OPÇÕES ____________________

        [v] .................... Voltar ao menu principal
        [1] ...................... Cadastrar funcionários
        [2] .......... Editar dados do funcionário por ID
        [3] .................. Excluir funcionário por ID
    *********************************************************

    >>> Digite a opção: """)
            if opcao == 'v':
                print('\n - VOLTANDO AO MENU PRINCIPAL!!! - \n')
                break
            elif opcao == '1':
                print('\n - CADASTRAR FUNCIONÁRIOS - \n')
                cadastrar_funcionario()
            elif opcao == '2':
                print('\n - EDITAR DADOS DO FUNCIONÁRIO - \n')
                editar_funcionario()
            elif opcao == '3':
                print('\n - EXCLUIR FUNCIONÁRIO POR ID - \n')
                excluir_funcionario()
            else:
                print('\n - OPÇÃO INVÁLIDA!!! - \n')

    def cadastrar_funcionario():
        """
        - Função para cadastrar funcionário na tabela funcionarios;
        - Não recebe parâmetros;
        - Exemplo de uso:
        >>> cadastrar_funcionario():
        """
        cargo_funcionario = input("""
*************************************************
    [v] .............................. Voltar

    __________ CARGOS DISPONÍVEIS ___________

    [1] ........... Assistente administrativo
    [2] ............. Representante de vendas
    [3] ....................... Recepcionista
    [4] ........................... Atendente
*************************************************

>>> Digite o cargo do funcionário: """)
        if cargo_funcionario == 'v':
            print('\n - VOLTANDO AO MENU OPÇÕES -> FUNCIONÁRIOS!!! - \n')
            return
        elif cargo_funcionario == '1':
            cargo_funcionario = 'Assistente administrativo'
        elif cargo_funcionario == '2':
            cargo_funcionario = 'Representante de vendas'
        elif cargo_funcionario == '3':
            cargo_funcionario = 'Recepcionista'
        elif cargo_funcionario == '4':
            cargo_funcionario = 'Atendente'
        else:
            print('\n - OPÇÃO INVÁLIDA!!! - \n')
            return
        
        nome_funcionario = input("Digite o nome do funcionário: ")
        cpf_funcionario = input("Digite o CPF do funcionário: ")
        data_admissao = input("Digite a data de admissão do funcionário: ")
        salario_funcionario = input("Digite o salário do funcionário: ")
        email_funcionario = input("Digite o email do funcionário: ")
        endereco_funcionario = input("Digite o endereço do funcionário: ")

        cursor.execute('''
                            INSERT INTO funcionarios VALUES (null, ?, ?, ?, ?, ?, ?, ?)
                        ''', (cargo_funcionario, nome_funcionario, cpf_funcionario, data_admissao, salario_funcionario, email_funcionario, endereco_funcionario))
        conexao_db.commit()

        print(f'\n - FUNCIONÁRIO > {nome_funcionario} < CADASTRADO!!! - \n')

    def editar_funcionario():
        """
        - Função para editar os dados do funcionário, buscando-o pela chave(id_funcionario) no dicionário "cadastros" e permitindo alterar o cargo, nome, data de admissão, salário, contato e endereço;
        - Não recebe parâmetro;
        - Exemplo de uso:
        >>> editar_funcionario():
        """
        ID_funcionario = input('ID(funcionário): ')
        cursor.execute (''' SELECT *
                            FROM funcionarios
                            WHERE id_funcionario = ?
                        ''', (ID_funcionario,))
        resultado = cursor.fetchone()
        if resultado:
            opcao = input("""
            ************************************************
                ________________ OPÇÕES ________________

                [v] ............................. Voltar
                [1] ...................... Alterar cargo
                [2] ....................... Alterar nome
                [3] ........................ Alterar CPF
                [4] ........... Alterar data de admissão
                [5] .................... Alterar salário
                [6] ............ Alterar contato (email)
                [7] ................... Alterar endereço
            ************************************************

            >>> Digite a opção: """)

            if opcao == 'v':
                print('\n - VOLTANDO!!! - \n')
                return
            elif opcao == '1':
                novo_cargo_funcionario = input('''
*************************************************
    [v] .............................. Voltar

    __________ CARGOS DISPONÍVEIS ___________

    [1] ........... Assistente administrativo
    [2] ............. Representante de vendas
    [3] ....................... Recepcionista
    [4] ........................... Atendente
*************************************************

>>> Digite o cargo do funcionário: ''')
                if novo_cargo_funcionario == 'v':
                    print('\n - VOLTANDO AO MENU OPÇÕES -> FUNCIONÁRIOS!!! - \n')
                    return
                elif novo_cargo_funcionario == '1':
                    novo_cargo_funcionario = 'Assistente administrativo'
                elif novo_cargo_funcionario == '2':
                    novo_cargo_funcionario = 'Representante de vendas'
                elif novo_cargo_funcionario == '3':
                    novo_cargo_funcionario = 'Recepcionista'
                elif novo_cargo_funcionario == '4':
                    novo_cargo_funcionario = 'Atendente'
                else:
                    print('\n - OPÇÃO INVÁLIDA!!! - \n')
                    return
                cursor.execute (''' UPDATE funcionarios
                                    SET cargo_funcionario = ?
                                    WHERE id_funcionario = ?
                                ''', (novo_cargo_funcionario, ID_funcionario))
                print('\n - ALTERAÇÃO CONCLUÍDA!!! - \n')
            elif opcao == '2':
                novo_nome_funcionario = input("Novo nome do funcionário: ")
                cursor.execute (''' UPDATE funcionarios
                                    SET nome_funcionario = ?
                                    WHERE id_funcionario = ?
                                ''', (novo_nome_funcionario, ID_funcionario))
                conexao_db.commit()
                print('\n - ALTERAÇÃO CONCLUÍDA!!! - \n')
            elif opcao == '3':
                novo_cpf_funcionario = input("Novo CPF do funcionário: ")
                cursor.execute (''' UPDATE funcionarios
                                    SET cpf_funcionario = ?
                                    WHERE id_funcionario = ?
                                ''', (novo_cpf_funcionario, ID_funcionario))
                conexao_db.commit()
                print('\n - ALTERAÇÃO CONCLUÍDA!!! - \n')
            elif opcao == '4':
                nova_data_admissao = input("Nova data admissão: ")
                cursor.execute (''' UPDATE funcionarios
                                    SET data_admissao = ?
                                    WHERE id_funcionario = ?
                                ''', (nova_data_admissao, ID_funcionario))
                conexao_db.commit()
                print('\n - ALTERAÇÃO CONCLUÍDA!!! - \n')
            elif opcao == '5':
                novo_salario = input("Novo salário do funcionário: ")
                cursor.execute (''' UPDATE funcionarios
                                    SET salario_funcionario = ?
                                    WHERE id_funcionario = ?
                                ''', (novo_salario, ID_funcionario))
                conexao_db.commit()
                print('\n - ALTERAÇÃO CONCLUÍDA!!! - \n')
            elif opcao == '6':
                novo_email_funcionario = input("Novo email do funcionário: ")
                cursor.execute (''' UPDATE funcionarios
                                    SET email_funcionario = ?
                                    WHERE id_funcionario = ?
                                ''', (novo_email_funcionario, ID_funcionario))
                conexao_db.commit()
                print('\n - ALTERAÇÃO CONCLUÍDA!!! - \n')
            elif opcao == '7':
                novo_endereco_funcionario = input("Novo endereco do funcionário: ")
                cursor.execute (''' UPDATE funcionarios
                                    SET endereco_funcionario = ?
                                    WHERE id_funcionario = ?
                                ''', (novo_endereco_funcionario, ID_funcionario))
                conexao_db.commit()
                print('\n - ALTERAÇÃO CONCLUÍDA!!! - \n')
        else:
            print(f'\n - ID {ID_funcionario} INEXISTENTE!!! - \n')

    def excluir_funcionario():
        """
        - Função para excluir um funcionário da tabela funcionarios, buscando-o pela PK(id_funcionario);
        - Não recebe parâmetro;
        - Exemplo de uso:
        >>> excluir_funcionario()
        """
        ID_funcionario = input("ID(funcionário):")
        cursor.execute (''' DELETE FROM funcionarios
                            WHERE id_funcionario = ?
                        ''',(ID_funcionario,))
        conexao_db.commit()
        print(f'\n - FUNCIONÁRIO {ID_funcionario} EXCLUÍDO!!! - \n')

    menu_funcionarios()

if __name__ == '__main__':
    cadastro_funcionarios()
