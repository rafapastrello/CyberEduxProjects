# PASTRELLO
import os
import json

def cadastrar_funcionarios():
    """
    Função responsável por cadastrar os funcionários de uma locadora de veículos.

    O usuário pode escolher entre as seguintes opções:
    v. Para voltar ao menu principal.
    1. Cadastrar funcionárioS - Para adicionar um funcionário à lista.
    2. Excluir funcionário - Para excuir um funcionário da lista.
    3. Editar Funcionário - Para editar alguma informação do funcionário.

    A função entra em um loop, exibindo o menu e aguardando a entrada do usuário.
    Com base na escolha do usuário, a função direciona para a função correspondente.

    Não são necessários argumentos de entrada para esta função.

    Exemplo de uso:
    >>> cadastrar_funcionarios()
    """

    def menu():
        cadastros = dict()
        
        while True:
            opcao = input("""
    **********************************************
        _______________ OPÇÕES _______________
        
        [v] ......... Voltar ao menu principal
        [1] ........... Cadastrar funcionários
        [2] .............. Listar funcionários
        [3] ....... Buscar funcionário por CPF
        [4] .............. Excluir funcionário
        [5] ........................... Salvar
        [6] ......................... Carregar
    **********************************************

    >>> Digite a opção: """)
            if opcao == 'v':
                print('\n - VOLTANDO AO MENU PRINCIPAL!!! - \n')
                break
            elif opcao == '1':
                print('\n - CADASTRAR FUNCIONÁRIOS - \n')
                cadastrar(cadastros)
            elif opcao == '2':
                print('\n - LISTAR FUNCIONÁRIOS - \n')
                listagem(cadastros)
            elif opcao == '3':
                print('\n - BUSCAR FUNCIONÁRIO POR CPF - \n')
                buscar(cadastros)
            elif opcao == '4':
                print('\n - EXCLUIR FUNCIONÁRIO POR CPF - \n')
                excluir()
            elif opcao == '5':
                print('\n - SALVAR - \n')
                salvar(cadastros)
            elif opcao == '6':
                print('\n - CARREGAR - \n')
                retorno = carregar()
                if retorno is not None:
                    cadastros = retorno
            else:
                print('\n - OPÇÃO INVÁLIDA!!! - \n')

    def cadastrar(cadastros):
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

        nome_funcionario = input('Digite o NOME do funcionário: ')
        cpf_funcionario = input('Digite o CPF do funcionário: ')
        data_admissão = input('Digite a DATA DE ADMISSÃO do funcionário: ')
        email_funcionario = input('Digite o EMAIL do funcionário: ')
        endereco_funcionario = input('Digite o ENDEREÇO do funcionário: ')

        cadastros[cpf_funcionario] = (cargo_funcionario, nome_funcionario, data_admissão, email_funcionario, endereco_funcionario)

    def listagem(cadastros):

        for rga in cadastros.keys():
            nome, email, turma = cadastros[rga]
            print(f'{rga:<4} {nome:<10} {email:<15} {turma:<3}')


        print('')
        print(f'{"ID(CPF)":<15} | {"CARGO":<15} | {"NOME":<20} | {"DATA ADMISSÂO":<20} | {"CONTATO(EMAIL)":<20} | {"ENDEREÇO":<20}')
        print("-" * 120)
        for cpf in cadastros.keys():
            print(f'{cpf:<6} | {cadastros[cpf][0]:<15} | {cadastros[cpf][1]:<17} | {cadastros[cpf][2]:<13} | {cadastros[cpf][3]:<15} | {cadastros[cpf][4]:<18}| {cadastros[cpf][5]:<13}')
        print('')

    def buscar(cadastros):
        rga = int(input('RGA: '))
        if rga in cadastros.keys():
            print(cadastros[rga])
        else:
            print('Veículo Inexistente !!')

    #def excluir():
        #pass

    def salvar(cadastros):
        with open("funcionarios",'w') as f:
            json.dump(clientes,f)

        #filename = input('Nome do Arquivo: ')
        #f = open(filename, 'w')
        #f.write(str(cadastros))
        #f.close()

    def carregar():
        filename = input('Nome do Arquivo: ')
        if os.path.exists(filename):
            f = open(filename, 'r')
            texto = f.read()
            f.close()
            return eval(texto)
        else:
            print('Arquivo Inexistente !!')
            return None

    menu()
    
if __name__ == '__main__':
    cadastrar_funcionarios()
