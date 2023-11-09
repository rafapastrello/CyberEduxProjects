import cad_clientes
import cad_funcionarios
import cad_veiculos
import locacao

def menu():
    """
    Função responsável por exibir um menu de opções para o sistema de uma locadora de veículos.

    O usuário pode escolher entre as seguintes opções:
    1. Locação - Para iniciar o processo de locação de veículos.
    2. Cadastrar Veículos - Para adicionar novos veículos ao sistema.
    3. Cadastrar Clientes - Para registrar informações sobre os clientes da locadora.
    4. Cadastrar Funcionários - Para incluir dados de funcionários da locadora.
    s. SAIR - Para encerrar o programa.

    A função entra em um loop, exibindo o menu e aguardando a entrada do usuário.
    Com base na escolha do usuário, a função direciona para a função correspondente ou encerra o programa.

    Não são necessários argumentos de entrada para esta função.

    Exemplo de uso:
    >>> menu()
    """

    while True:
        opcao = input("""
            ------------ LOCADORA VEÍCULOS -------------
             ******************************************
               ----------- MENU PRINCIPAL -----------
                -------------- opções --------------
                [s] ........................... SAIR
                [1] ............. Cadastrar Veículos
                [2] ............. Cadastrar Clientes
                [3] ........................ Locação
                [4] ......... Cadastrar Funcionários

            ********************************************

            >>> Escolha a opção: """)

        if opcao == 's':
            print('\n - PROGRAMA ENCERRADO COM SUCESSO! - \n')
            break
        elif opcao == '1':
            print('\n - CADASTRO DE VEÍCULOS - \n')
            cad_veiculos.cadastrar_veiculos()
        elif opcao == '2':
            print('\n - CADASTRO DE CLIENTES - \n')
            cad_clientes.cadastrar_clientes()
        elif opcao == '3':
            print('\n - LOCAÇÃO - \n')
            locacao.locacao()
        elif opcao == '4':
            print('\n - CADASTRO DE FUNCIONÁRIOS - \n')
            cad_funcionarios.cadastrar_funcionarios()
        else:
            print('\n - OPÇÃO INVÁLIDA! - \n')


if __name__ == '__main__':
    menu()