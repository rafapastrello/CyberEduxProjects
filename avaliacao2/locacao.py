# KHALIL

def locacao(): 
    # Função para obter a ID do cliente
    def obter_id_cliente():
        id_cliente = input("Digite a ID do cliente: ")
        return id_cliente

    # Função para obter a forma de pagamento
    def obter_forma_pagamento():
        while True:
            forma_pagamento = input("Digite a forma de pagamento (débito, crédito ou dinheiro): ")
            if forma_pagamento.lower() in ['débito', 'crédito', 'dinheiro']:
                return forma_pagamento.lower()
            else:
                print("Forma de pagamento inválida. Por favor, tente novamente.")

    # Função para obter o código do carro
    def obter_codigo_carro():
        codigo_carro = input("Digite o código do carro: ")
        return codigo_carro

    # Função para obter a quilometragem
    def obter_quilometragem():
        quilometragem = float(input("Digite a quilometragem: "))
        return quilometragem

    # Função principal para executar as etapas da locação
    def locacao_carro():
        # Criar um dicionário vazio para armazenar os clientes e suas informações
        clientes = {}

        while True:
            print("\nOpções:")
            print("1. Adicionar cliente")
            print("2. Visualizar clientes registrados")
            print("3. Editar cliente")
            print("4. Sair")
            escolha = input("Digite o número da opção desejada: ")

            if escolha == '1':
                id_cliente = obter_id_cliente()
                forma_pagamento = obter_forma_pagamento()
                codigo_carro = obter_codigo_carro()
                quilometragem = obter_quilometragem()

                # Adicionar as informações do cliente ao dicionário
                clientes[id_cliente] = {
                    'Forma de pagamento': forma_pagamento,
                    'Código do carro': codigo_carro,
                    'Quilometragem': quilometragem
                }
                print("Cliente adicionado com sucesso!")

            elif escolha == '2':
                print("\nClientes registrados:")
                for id_cliente, info in clientes.items():
                    print("ID do cliente:", id_cliente)
                    for chave, valor in info.items():
                        print(chave + ":", valor)

            elif escolha == '3':
                id_cliente = input("Digite a ID do cliente que deseja editar: ")

                if id_cliente in clientes:
                    print("\nOpções de edição:")
                    print("1. Editar forma de pagamento")
                    print("2. Editar código do carro")
                    print("3. Editar quilometragem")
                    escolha_edicao = input("Digite o número da opção que deseja editar: ")

                    if escolha_edicao == '1':
                        forma_pagamento = obter_forma_pagamento()
                        clientes[id_cliente]['Forma de pagamento'] = forma_pagamento

                    elif escolha_edicao == '2':
                        codigo_carro = obter_codigo_carro()
                        clientes[id_cliente]['Código do carro'] = codigo_carro

                    elif escolha_edicao == '3':
                        quilometragem = obter_quilometragem()
                        clientes[id_cliente]['Quilometragem'] = quilometragem

                    else:
                        print("Opção inválida.")

                else:
                    print("Cliente não encontrado.")

            elif escolha == '4':
                break

            else:
                print("Opção inválida.")

    # Chamada da função principal para iniciar a locação de carro
    locacao_carro()

if __name__ == '__main__':
    locacao_carro()
    