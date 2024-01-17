import cad_clientes
import cad_funcionarios
import cad_veiculos
import cad_locacao

def menu_locadora():
    """
    Função responsável por exibir um menu de opções para o sistema de uma locadora de veículos.

    O usuário pode escolher entre as seguintes opções:[s] SAIR - Para encerrar o programa, [1] Cadastrar Veículos - Para inserir novos veículos ao sistema, [2] Cadastrar Clientes - Para registrar informações sobre os clientes da locadora, [3] Locação de veículos - Para iniciar o processo de locação de veículos, [4] Cadastrar Funcionários - Para inserir dados de funcionários da locadora.

    - A função entra em um loop, exibindo o menu e aguardando a entrada do usuário;
    - Com base na escolha do usuário, a função direciona para a função correspondente ou encerra o programa;
    - Não recebe parâmetros;
    - Exemplo de uso:
    >>> menu_locadora()
    """

    while True:
        opcao = input("""
            ------------ LOCADORA VEÍCULOS -------------
             ******************************************
               ----------- MENU PRINCIPAL -----------
                -------------- opções --------------
                [s] ............... ENCERRAR SISTEMA
                [1] ............. Cadastrar Veículos
                [2] ............. Cadastrar Clientes
                [3] ............ Locação de veículos
                [4] ......... Cadastrar Funcionários

            ********************************************

            >>> Escolha a opção: """)

        if opcao == 's':
            print('\n - PROGRAMA ENCERRADO COM SUCESSO! - \n')
            break
        elif opcao == '1':
            print('\n - CADASTRO DE VEÍCULOS - \n')
            cad_veiculos.cadastro_veiculos()
        elif opcao == '2':
            print('\n - CADASTRO DE CLIENTES - \n')
            cad_clientes.cadastro_clientes()
        elif opcao == '3':
            print('\n - LOCAÇÃO DE VEÍCULOS - \n')
            cad_locacao.cadastro_locacoes()
        elif opcao == '4':
            print('\n - CADASTRO DE FUNCIONÁRIOS - \n')
            cad_funcionarios.cadastro_funcionarios()
        else:
            print('\n - OPÇÃO INVÁLIDA! - \n')

if __name__ == '__main__':
    menu_locadora()