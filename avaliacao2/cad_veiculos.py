# MARCUS

def cadastrar_veiculos():
    print('\n############## CADASTRO DE VEÍCULOS - Versão1.0 ##############')

    import os
    import json

    def cadastrar(cadastros):

        """
        ################################################
        # Função para fazer o cadastro do veículo      #
        #                                              #
        # Parametros:                                  #
        # Cadastros (dict) - dicionário de cadastros   #
        ################################################
        """

        fab_veiculo = input('Digite o Fabricante do Veículo: ')
        marca_veículo = input('Digite a Marca do Veículo: ')
        cor_veiculo = input('Digite a Cor do Veículo: ')
        ano_veiculo = input('Digite o Ano do Veículo: ')
        mod_veiculo = input('Digite o Ano do Modelo do Veículo: ')
        placa_veiculo = input('Digite a Placa do Veículo: ')
        diaria_veiculo = input('Digite o Valor da Diária do Veículo: ')


        if cadastros == dict():
            rga = 1
        else:
            rga = max(cadastros.keys())+1
        cadastros[rga] = (fab_veiculo, marca_veículo, cor_veiculo, ano_veiculo, mod_veiculo, placa_veiculo, diaria_veiculo)

    def listagem(cadastros):

        """
        ################################################
        # Função para mostrar os cadastros.            #
        #                                              #
        # Parametros:                                  #
        # Cadastros (dict) - dicionário de cadastros   #
        ################################################
        """

        for rga in cadastros.keys():
            print('RGA', rga, 'Dados', cadastros[rga])

    def buscar(cadastros):

        """
        ################################################
        # Função para busca do estudante por RGA.      #
        #                                              #
        # Parametros:                                  #
        # Cadastros (dict) - dicionário de cadastros   #
        ################################################
        """

        rga = int(input('RGA: '))
        if rga in cadastros.keys():
            print(cadastros[rga])
        else:
            print('Veículo Inexistente !!')

    def salvar(cadastros):

        """
        ################################################
        # Função para salvar cadastros em arquivo.     #
        #                                              #
        # Parametros:                                  #
        # Cadastros (dict) - dicionário de cadastros   #
        ################################################
        """

        filename = input('Nome do Arquivo: ')
        f = open(filename, 'w')
        f.write(json.dumps(cadastros))
        f.close()

    def carregar():

        """
        #########################################################
        # Função que retorna o dicionário salvo em um arquivo   #
        #                                                       #
        # Retorno:                                              #
        # Dict|NoneType: caso o arquivo exista, retorna         #
        # o dicionário. Caso não exista, retorna None.          #
        #########################################################
        """

        filename = input('Nome do Arquivo: ')
        if os.path.exists(filename):
            f = open(filename, 'r')
            texto = f.read()
            f.close()
            return json.loads(texto)
        else:
            print('Arquivo Inexistente !!')
            return None

    def menu():

        """
        #####################
        # Menu do Veículo   #
        #####################
        """

        cadastros = dict()
        while True:
            print('\n[1] - Cadastrar\n[2] - Listar\n[3] - Buscar RGA\n[4] - Salvar\n[5] - Carregar')
            opcao = input('\nDigite a Opção: ')
            if opcao == '1':
                cadastrar(cadastros)
            elif opcao == '2':
                listagem(cadastros)
            elif opcao == '3':
                buscar(cadastros)
            elif opcao == '4':
                salvar(cadastros)
            elif opcao == '5':
                retorno = carregar()
                if retorno is not None:
                    cadastros = retorno
            else:
                print('Opção Inválida !!')
    menu()

if __name__ == '__main__':
    menu()
