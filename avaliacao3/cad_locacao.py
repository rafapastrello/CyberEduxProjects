# ISIS

import sqlite3

conexao = sqlite3.connect('DB_Rent_A_Car.db')

sql = conexao.cursor()

sql.execute('''



  ''')


def cadastro_locacoes():
  """
    - Função responsável por fazer as locações de uma locadora de veículos;
    - O usuário pode escolher entre as seguintes opções:
    v. Para voltar ao menu principal.
    1. Locar Veículo - Para adicionar uma Locação à lista.
    2. Excluir Locação - Para excuir uma Locação da lista.
    3. Editar Locação - Para editar alguma informação da Locação.
    - A função entra em um loop, exibindo o menu e aguardando a entrada do usuário;
    - Com base na escolha do usuário, a função direciona para a função correspondente;
    - Não são necessários argumentos de entrada para esta função.
    - Exemplo de uso:
    >>> cadastro_locacoes()
    """

  def menu_locacao():
    """
            - Função para exibir o menu principal do arquivo, que possui as opções: [v] Voltar ao menu principal, 
            [1] Locar veículo, [2] Listar locações, [3] Buscar locações por ID,
            [4] Editar dados da locação por ID, [5] Excluir locação por ID, [6] Salvar arquivo e 
            [7] Carregar arquivo;
            - Não recebe parâmetros;
            - Exemplo de uso:
            >>> menu_locacao():
        """

    while True:
      opcao = input("""
    *********************************************************
        ____________________ OPÇÕES ____________________

        [v] .................... Voltar ao menu principal
        [1] ............................... Locar veículo
        [2] .............. Editar dados da locação por ID
        [3] ...................... Excluir locação por ID
    *********************************************************

    >>> Digite a opção: """)
      if opcao == 'v':
        print('\n - VOLTANDO AO MENU PRINCIPAL!!! - \n')
        break
      elif opcao == '1':
        print('\n - LOCAR VEÍCULO - \n')
        locar_veiculo()
      elif opcao == '2':
        print('\n - EDITAR DADOS DA LOCAÇÃO POR ID - \n')
        editar_locacao()
      elif opcao == '3':
        print('\n - EXCLUIR LOCAÇÃO POR ID - \n')
        excluir_locacao()
      else:
        print('\n - OPÇÃO INVÁLIDA!!! - \n')

  # função para cadastrar a locação

  def locar_veiculo():
    """
    - Função para cadastrar locação na tabela locacoes;
    - Não recebe parâmetros;
    - Exemplo de uso:
    >>> locar_veiculo():
    """
    
    id_cliente = input('Digite o ID do cliente: ')
    id_veiculo = int(input('Digite o ID do veículo: '))
    id_funcionario = input('Digite o ID do funcionario')
    data_retirada = input('Digite a data de retirada do veículo: ')
    qtd_diarias = int(input(' numero de diarias:'))
    data_devolucao = input('Digite a data de devolução do veículo: ')
    forma_pagamento = input(" forma de pagamento: ")

    sql.execute(
        '''

        SELECT valor_diaria_veiculo from veiculos WHERE id_veiculo=?
        ''', (id_veiculo, ))

    resultado = sql.fetchone()
    valor_diario = resultado[0]
    valor_pagar = valor_diario * qtd_diarias

    sql.execute(
        ''' INSERT INTO locacoes (id_locacao,fk_id_cliente,fk_id_veiculo,fk_id_funcionario,data_retirada,qtd_diarias,data_devolucao,valor_pagar,forma_pagamento ) VALUES (null,?,?,?,?,?,?,?,?)''',
        (id_cliente,id_veiculo,id_funcionario,data_retirada,qtd_diarias,data_devolucao,valor_pagar,forma_pagamento))
    conexao.commit()

#funcão para editar a tabela locacao
  def editar_locacao():
    id_locacao = input('Digite o ID da locacao: ')

    opcao = int(
        input("""
        ******
            __ OPÇÕES __

        1 --> ID cliente
        2 --> ID veiculo 
        3 --> ID funcionario
        4 --> data de retirada
        5 --> data de devolução
        6 --> quantidade de diaria
        7 --> forma de pagamento
        ******

        >>> Digite a opção: """))

    novoAtributo = input(" Dejesa mudar esse atrubuto para:")

    dicionario = {
        1: 'fk_cliente',
        2: 'fk_veiculo',
        3: 'fk_funcionario',
        4: 'data_retirada',
        5: 'data_devolucao',
        6: 'quant_diarias',
        7: 'forma_pagamento'
    }

    sql.execute(f"UPDATE locacoes set {dicionario[opcao]} =? WHERE id_locacao = ?  ",
                (novoAtributo, id_locacao))

    print('=' * 40)
    print("Esse elemento foi alterado!")

    conexao.commit()

  # função para excluir locação

  def excluir_locacao():

    deletar = input(("Digite o ID da locação:"))

    sql.execute(" DELETE FROM locacoes WHERE id_locacao = ?", (deletar, ))

    print("=" * 30)
    print(" Esta locação foi deletada !")

    conexao.commit()

  menu_locacao()

if __name__ == '__main__':
  cadastro_locacoes()
