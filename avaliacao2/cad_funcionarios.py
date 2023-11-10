# PASTRELLO

import os
import json

def cadastrar_funcionarios():
    """
    - Função responsável por cadastrar os funcionários de uma locadora de veículos;
    - O usuário pode escolher entre as seguintes opções:
    v. Para voltar ao menu principal.
    1. Cadastrar funcionárioS - Para adicionar um funcionário à lista.
    2. Excluir funcionário - Para excuir um funcionário da lista.
    3. Editar Funcionário - Para editar alguma informação do funcionário.
    - A função entra em um loop, exibindo o menu e aguardando a entrada do usuário;
    - Com base na escolha do usuário, a função direciona para a função correspondente;
    - Não são necessários argumentos de entrada para esta função.
    - Exemplo de uso:
    >>> cadastrar_funcionarios()
    """

    def menu():
        """
            - Função para exibir o menu principal do arquivo, que possui as opções: [v] Voltar ao menu principal, 
            [1] Cadastrar funcionários, [2] Listar funcionários, [3] Buscar funcionário por CPF,
            [4] Editar dados do funcionário por CPF, [5] Excluir funcionário por CPF, [6] Salvar arquivo e 
            [7] Carregar arquivo;
            - Não recebe parâmetros;
            - Exemplo de uso:
            >>> menu():
        """
        cadastros = dict()

        while True:
            opcao = input("""
    *********************************************************
        ____________________ OPÇÕES ____________________

        [v] .................... Voltar ao menu principal
        [1] ...................... Cadastrar funcionários
        [2] ......................... Listar funcionários
        [3] .................. Buscar funcionário por CPF
        [4] ......... Editar dados do funcionário por CPF
        [5] ................. Excluir funcionário por CPF
        [6] .............................. Salvar arquivo
        [7] ............................ Carregar arquivo
    *********************************************************

    >>> Digite a opção: """)
            if opcao == 'v':
                print('\n - VOLTANDO AO MENU PRINCIPAL!!! - \n')
                break
            elif opcao == '1':
                print('\n - CADASTRAR FUNCIONÁRIOS - \n')
                cadastrar(cadastros)
            elif opcao == '2':
                print('\n - LISTAR FUNCIONÁRIOS - \n')
                listar(cadastros)
            elif opcao == '3':
                print('\n - BUSCAR FUNCIONÁRIO POR CPF - \n')
                buscar(cadastros)
            elif opcao == '4':
                print('\n - EDITAR DADOS DO FUNCIONÁRIO - \n')
                editar(cadastros)
            elif opcao == '5':
                print('\n - EXCLUIR FUNCIONÁRIO POR CPF - \n')
                excluir(cadastros)
            elif opcao == '6':
                print('\n - SALVAR - \n')
                salvar(cadastros)
            elif opcao == '7':
                print('\n - CARREGAR - \n')
                carregar(cadastros)
                #if retorno is not None:
                #    cadastros = retorno
            else:
                print('\n - OPÇÃO INVÁLIDA!!! - \n')

    def cadastrar(cadastros):
        """
            - Função para cadastrar funcionário no dicionário pré-definido "cadastros";
            - Recebe o parâmetro (cadastros);
            - Exemplo de uso:
            >>> cadastrar(cadastros):
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

        nome_funcionario = input('Digite o NOME do funcionário: ')
        cpf_funcionario = input('Digite o CPF do funcionário: ')
        data_admissão = input('Digite a DATA DE ADMISSÃO do funcionário: ')
        salario_funcionario = input('Digite o SALÁRIO do funcionário: ')
        email_funcionario = input('Digite o EMAIL do funcionário: ')
        endereco_funcionario = input('Digite o ENDEREÇO do funcionário: ')

        cadastros[cpf_funcionario] = [cargo_funcionario, nome_funcionario, data_admissão, salario_funcionario, email_funcionario, endereco_funcionario]
        print('\n - FUNCIONÁRIO CADASTRADO!!! - \n')

    def listar(cadastros):
        """
            - Função para exibir uma tabela dos funcionários cadastrados no dicionário "cadastros" no terminal;
            - Recebe o parâmetro (cadastros);
            - Exemplo de uso:
            >>> listar(cadastros):
        """
        print(f'{"ID(CPF)":<14} | {"CARGO":<25} | {"NOME":<15} | {"DATA ADMISSÂO":<13} | {"SALÁRIO":<9} | {"CONTATO(EMAIL)":<22} | {"ENDEREÇO":<20}')
        print("-" * 125)
        for cpf in cadastros.keys():
            print(f'{cpf:<14} | {cadastros[cpf][0]:<25} | {cadastros[cpf][1]:<15} | {cadastros[cpf][2]:<13} | {cadastros[cpf][3]:<9} | {cadastros[cpf][4]:<22} | {cadastros[cpf][5]:<20}')

    def buscar(cadastros):
        """
            - Função para buscar um funcionário pela chave(CPF) no dicionário "cadastros";
            - Recebe o parâmetro (cadastros);
            - Exemplo de uso:
            >>> buscar(cadastros):
        """
        cpf = input('CPF: ')
        if cpf in cadastros.keys():
            print(cadastros[cpf])
        else:
            print('\n - CPF INEXISTENTE!!! - \n')

    def editar(cadastros):
        """
            - Função para editar os dados do funcionário, buscando-o pela chave(CPF) no dicionário "cadastros" e permitindo alterar o cargo, nome, data de admissão, salário, contato e endereço;
            - Recebe o parâmetro (cadastros);
            - Exemplo de uso:
            >>> editar(cadastros):
        """
        cpf = input('CPF: ')
        if cpf in cadastros.keys():
            opcao = input("""
        ************************************************
            ________________ OPÇÕES ________________

            [v] ............................. Voltar
            [1] ...................... Alterar cargo
            [2] ....................... Alterar nome
            [3] ........... Alterar data de admissão
            [4] .................... Alterar salário
            [5] ............ Alterar contato (email)
            [6] ................... Alterar endereço
        ************************************************

        >>> Digite a opção: """)
        
            if opcao == 'v':
                print('\n - VOLTANDO!!! - \n')
                return
            elif opcao == '1':
                print('\n - ALTERAR CARGO - \n')
                cargo_funcionario = input("""
        *************************************************
            [v] .............................. Voltar

            __________ CARGOS DISPONÍVEIS ___________

            [1] ........... Assistente administrativo
            [2] ............. Representante de vendas
            [3] ....................... Recepcionista
            [4] ........................... Atendente
        *************************************************

        >>> Digite o novo cargo do funcionário: """)
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
                cadastros[cpf][0] = cargo_funcionario
                print('\n - ALTERAÇÃO CONCLUÍDA!!! - \n')

            elif opcao == '2':
                print('\n - ALTERAR NOME - \n')
                nome_funcionario = input('Novo nome: ')
                cadastros[cpf][1] = nome_funcionario
                print('\n - ALTERAÇÃO CONCLUÍDA!!! - \n')
            elif opcao == '3':
                print('\n - ALTERAR DATA DE ADMISSÃO - \n')
                data_admissão = input('Nova data de admissão: ')
                cadastros[cpf][2] = data_admissão
                print('\n - ALTERAÇÃO CONCLUÍDA!!! - \n')
            elif opcao == '4':
                print('\n - ALTERAR SALÁRIO - \n')
                salario_funcionario = input('Novo salário: ')
                cadastros[cpf][3] = salario_funcionario
                print('\n - ALTERAÇÃO CONCLUÍDA!!! - \n')
            elif opcao == '5':
                print('\n - ALTERAR CONTATO (email) - \n')
                email_funcionario = input('Novo email: ')
                cadastros[cpf][4] = email_funcionario
                print('\n - ALTERAÇÃO CONCLUÍDA!!! - \n')
            elif opcao == '6':
                print('\n - ALTERAR ENDEREÇO - \n')
                endereco_funcionario = input('Novo endereço: ')
                cadastros[cpf][5] = endereco_funcionario
                print('\n - ALTERAÇÃO CONCLUÍDA!!! - \n')
            else:
                print('\n - OPÇÃO INVÁLIDA!!! - \n')

        else:
            print('\n - CPF INEXISTENTE!!! - \n')

    def excluir(cadastros):
        """
            - Função para excluir um funcionário pela chave(CPF) no dicionário "cadastros";
            - Recebe o parâmetro (cadastros);
            - Exemplo de uso:
            >>> excluir(cadastros):
        """
        cpf = input("CPF:")
        if cpf in cadastros.keys():
            deletar = cadastros.pop(cpf)
            print('\n - FUNCIONÁRIO EXCLUÍDO!!! - \n')
            return deletar
        else:
            print('\n - CPF INEXISTENTE!!! - \n')
            return

    def salvar(cadastros):
        """
            - Função para salvar os dados cadastrados no dicionario "cadastros";
            - Recebe o parâmetro (cadastros);
            - Exemplo de uso:
            >>> salvar(cadastros):
        """
        filename = input('Nome do arquivo: ')
        f = open(filename, 'w')
        f.write(json.dumps(cadastros))
        f.close()

        print(f'\n - ARQUIVO " {filename} " SALVO!!! - \n')

    def carregar(cadastros):
        """
            - Função para buscar um funcionário pela chave(CPF) no dicionário "cadastros";
            - Recebe o parâmetro (cadastros);
            - Exemplo de uso:
            >>> buscar(cadastros):
        """
        filename = input('Nome do arquivo: ')
        if os.path.exists(filename):
            f = open(filename, 'r')
            texto = f.read()
            f.close()
            cadastros.clear()
            cadastros.update(json.loads(texto))
            print('\n - ARQUIVO CARREGADO!!! - \n')
        else:
            print('\n - ARQUIVO INEXISTENTE!!! - \n')
        
    menu()

if __name__ == '__main__':
    cadastrar_funcionarios()
